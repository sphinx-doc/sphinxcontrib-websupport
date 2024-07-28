from __future__ import annotations

from missing_module import missing_name
from missing_package3.missing_module3 import missing_name  # NoQA: F811


@missing_name
def decoratedFunction():
    """decoratedFunction docstring"""
    return None


class TestAutodoc:
    """TestAutodoc docstring."""
    @missing_name
    def decoratedMethod(self):
        """TestAutodoc::decoratedMethod docstring"""
        return None
