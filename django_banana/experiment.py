import random
import re
from .keying import get_key_for_experiment
from .option import Option


EXPERIMENT_PARSING_EXPRESSION = re.compile('^(\d+)\:(.*?)$')


class Experiment(object):
    """Experiment binding.

    Represents a single experiment bound to a session. An experiment is
    globally identified by its unique identifier and a generation number. Any
    modification to an experiment should involve a bump in generation resulting
    in redistribution of experiments. Experiment options are represented by
    experiment-unique identifiers and an optional weight.

    The option selection is lazily handled and will only be performed when the
    selection is actually accesed by a call to :func:`get_selected`.
    """

    def __init__(self, session, identifier, generation, options):
        """Initialize a new experiment binding.

        :param session: Session to which the experiment is bound.
        :param identifier:
            Globally unique experiment identifier. Should only contain
            alphanumeric characters and underscores for naming consistency.
        :param generation: Integer experiment generation starting from 1.
        :param options:
            Experiment options expressed either as a :class:`dict` mapping
            identifiers to either numerical weights or tuples of numerical
            weights and a :class:`dict` contining extra information for the
            option, or, alternatively, a :class:`list` of identifiers with
            equal weight or :class:`Option` instances.
        """

        self.session = session
        self.identifier = identifier
        self.generation = generation
        self._selected = None

        if isinstance(options, dict):
            self.options = {
                k: Option(k, *v) if isinstance(v, tuple) else Option(k, v)
                for k, v in options.items()
            }
        elif isinstance(options, (list, tuple, )):
            self.options = {}
            for o in options:
                if isinstance(o, Option):
                    self.options[o.identifier] = o
                else:
                    self.options[o] = Option(o)
        else:
            raise TypeError('cannot construct option distribution '
                            'from %r' % (options))

    def get_selected(self):
        """Get the selected option for the current session.

        :returns: a :class:`Option` representing the selected option.
        """

        # If we already have a selection, return it immediately.
        if self._selected is not None:
            return self._selected

        # Attempt to retrieve the selection from the session.
        session_key = get_key_for_experiment(self.identifier)
        session_data = self.session.get(session_key)

        if session_data is not None:
            data_match = EXPERIMENT_PARSING_EXPRESSION.match(session_data)
            if data_match and \
                    int(data_match.group(1)) == self.generation and \
                    data_match.group(2) in self.options:
                self._selected = self.options[data_match.group(2)]
                return self._selected

        # Assign a new option to the session.
        score_multiplier = 1.0 / float(sum(map(lambda o: o.weight,
                                               self.options.values())))
        chosen_score = random.random()

        score_sum = 0.0
        for index, option in enumerate(self.options.values()):
            score_addition = float(option.weight) * score_multiplier
            if chosen_score <= score_sum + score_addition or \
                    index == len(self.options) - 1:
                self.session[session_key] = '%d:%s' % (self.generation,
                                                       option.identifier)
                self._selected = option
                return option
            score_sum += score_addition
