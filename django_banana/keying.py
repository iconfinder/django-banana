from django.conf import settings


def get_key_for_experiment(identifier):
    """Get the session key for an experiment.

    :param identifier: Globally unique experiment identifier.
    """

    return '%s%s' % (getattr(settings,
                             'BANANA_SESSION_KEY_PREFIX',
                             'banana:'),
                     identifier)
