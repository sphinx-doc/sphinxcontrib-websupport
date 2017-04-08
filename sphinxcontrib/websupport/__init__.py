# -*- coding: utf-8 -*-
"""
    sphinxcontrib.websupport
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A Python API to easily integrate Sphinx documentation into Web
    applications.

    :copyright: Copyright 2007-2017 by the Sphinx team, see README.
    :license: BSD, see LICENSE for details.
"""

__import__('pkg_resources').declare_namespace(__name__)

__version_info__ = (1, 0, 0)
__version__ = '.'.join(str(v) for v in __version_info__)

from sphinxcontrib.websupport.core import WebSupport  # NOQA
