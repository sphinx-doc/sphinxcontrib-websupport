import pytest


__all__ = (
    'skip_unless_importable',
)


def skip_unless_importable(module, msg=None):
    """Decorator to skip test if module is not importable."""
    try:
        __import__(module)
    except ImportError:
        return pytest.mark.skipif(True, reason=(msg or 'conditional skip'))
    else:
        return pytest.mark.skipif(False, reason=(msg or 'conditional skip'))
