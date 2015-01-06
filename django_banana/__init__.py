"""Django Banana - delicious split testing.

Banana is a pure backend split testing addition to Django, which exposes
experiment selections in the template context to be handled by frontend
data collection frameworks. Actual experiment option selection is stored using
the built-in Django sessions.

Note: yes, the name is awesome.
"""

from .option import Option


__all__ = (
    Option.__name__,
)
