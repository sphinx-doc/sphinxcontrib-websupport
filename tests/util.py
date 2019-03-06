# -*- coding: utf-8 -*-
"""
    Sphinx test suite utilities
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2007-2018 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import os
import tempfile

import pytest

from sphinx.testing.path import path


__all__ = [
    'rootdir', 'tempdir',
    'skip_unless_importable',
]


rootdir = path(__file__).abspath().parent
if 'SPHINX_TEST_TEMPDIR' in os.environ:
    tempdir = path(os.environ['SPHINX_TEST_TEMPDIR']).abspath()
else:
    tempdir = path(tempfile.mkdtemp()).abspath()


def skip_unless_importable(module, msg=None):
    """Decorator to skip test if module is not importable."""
    try:
        __import__(module)
    except ImportError:
        return pytest.mark.skipif(True, reason=(msg or 'conditional skip'))
    else:
        return pytest.mark.skipif(False, reason=(msg or 'conditional skip'))
