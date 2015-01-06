from .experiment import Experiment


class ExperimentManager(object):
    """Experiment manager.

    Convenient session bound experiment manager.
    """

    def __init__(self, session):
        """Initialize an experiment manager.

        :param sesion: Session.
        """

        self.session = session
        self.experiments = {}

    def add(self, identifier, generation, options):
        """Add an experiment to the session.

        :param session: Session to which the experiment is bound.
        :param identifier:
            Globally unique experiment identifier. Should only contain
            alphanumeric characters and underscores for naming consistency.
        :param generation: Integer experiment generation starting from 1.
        :param options:
            Experiment options expressed either as a :class:`dict` mapping
            identifiers to numerical weights or, alternatively, a :class:`list`
            of identifiers with equal weight.
        :returns:
            the session bound experiment as a :class:`Experiment` instance.
        :raises KeyError:
            if an experiment with the same identifier is already registered.
        """

        if identifier in self.experiments:
            raise KeyError('an experiment with the identifier %s already '
                           'exists' % (identifier))

        self.experiments[identifier] = experiment = Experiment(self.session,
                                                               identifier,
                                                               generation,
                                                               options)

        return experiment

    def __getitem__(self, identifier):
        return self.experiments[identifier]
