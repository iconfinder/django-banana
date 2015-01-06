from .manager import ExperimentManager


class ExperimentsMiddleware(object):
    """Experiments middleware.

    Binds the convenient :class:`ExperimentManager` to the request.
    """

    def process_request(self, request):
        assert hasattr(request, 'session'), \
            'Django Banana requires session middleware to be installed'

        request.experiments = ExperimentManager(request.session)
