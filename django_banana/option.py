class Option(object):
    """Experiment option.

    :ivar identifier: Option identifier.
    :ivar weight: Numerical weight.
    :ivar extra: Extra option data as :class:`dict`.
    """

    def __init__(self, identifier, weight=1, extra=None):
        """Initialize a new experiment option.

        :param identifier: Option identifier.
        :param weight: Numerical weight. Default 1.
        :param extra: Extra option data as :class:`dict`.
        """

        self.identifier = identifier
        self.weight = weight
        self.extra = extra or {}

    def __repr__(self):
        return '<Option: %s (weight = %d, extra = %r)>' % (self.identifier,
                                                           self.weight,
                                                           self.extra)
