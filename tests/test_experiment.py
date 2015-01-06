from unittest import TestCase
from django_banana.experiment import Experiment


def get_valid_experiments(session):
    return [
        Experiment(session, 'non_weighted', 1, ['a', 'b', 'c']),
        Experiment(session, 'weighted', 5, {
            'a': 99,
            'b': 5,
            'c': 2.3
        }),
    ]


class ExperimentTestCase(TestCase):
    """Test case for :class:`Experiment`.
    """

    def test_init__invalid__raises_expected(self):
        """Experiment(<invalid>) raises expected exception
        """

        pass

    def test_init__valid__succeeds(self):
        """Experiment(<valid>) succeeds
        """

        get_valid_experiments({})

    def test_get_selected__not_in_session__returns_option(self):
        """Experiment(<not in session>).get_selected() returns random option
        """

        session = {}

        for experiment in get_valid_experiments(session):
            self.assertFalse('banana:%s' % (experiment.identifier) in session)

            selected = experiment.get_selected()
            self.assertIn(selected.identifier, experiment.options.keys())
            self.assertTrue('banana:%s' % (experiment.identifier) in session)
            self.assertEqual(session['banana:%s' % (experiment.identifier)],
                             '%d:%s' % (experiment.generation,
                                        selected.identifier))

            for _ in xrange(100):
                self.assertEqual(experiment.get_selected(), selected)

    def test_get_selected__in_session__returns_stored(self):
        """Experiment(<in session>).get_selected() returns stored option
        """

        session = {
            'banana:non_weighted': '1:c',
            'banana:weighted': '5:c',
        }

        for experiment in get_valid_experiments(session):
            for _ in xrange(100):
                self.assertEqual(experiment.get_selected().identifier, 'c')

    def test_get_selected__invalid_in_session__returns_new(self):
        """Experiment(<invalid in session>).get_selected() returns new option
        """

        session = {
            'banana:non_weighted': '1:d',
            'banana:weighted': '5:d',
        }

        for experiment in get_valid_experiments(session):
            selected = experiment.get_selected()
            self.assertIn(selected.identifier, experiment.options.keys())
            self.assertTrue('banana:%s' % (experiment.identifier) in session)
            self.assertEqual(session['banana:%s' % (experiment.identifier)],
                             '%d:%s' % (experiment.generation,
                                        selected.identifier))

    def test_get_selected__old_generation_in_session__returns_new(self):
        """Experiment(<old gen. in session>).get_selected() returns new option
        """

        session = {
            'banana:non_weighted': '0:c',
            'banana:weighted': '4:c',
        }

        for experiment in get_valid_experiments(session):
            selected = experiment.get_selected()
            self.assertIn(selected.identifier, experiment.options.keys())
            self.assertTrue('banana:%s' % (experiment.identifier) in session)
            self.assertEqual(session['banana:%s' % (experiment.identifier)],
                             '%d:%s' % (experiment.generation,
                                        selected.identifier))


__all__ = ('ExperimentTestCase', )
