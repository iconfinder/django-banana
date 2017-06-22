from .manager import ExperimentManager


class ExperimentsMiddleware(object):
    """Experiments middleware.

    Binds the convenient :class:`ExperimentManager` to the request.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        assert hasattr(request, 'session'), \
            'Django Banana requires session middleware to be installed'

        request.experiments = ExperimentManager(request.session)
        # Get response from later middleware.
        response = self.get_response(request)

        return response
