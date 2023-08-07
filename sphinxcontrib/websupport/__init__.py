# -*- coding: utf-8 -*-
"""
    sphinxcontrib.websupport
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A Python API to easily integrate Sphinx documentation into Web
    applications.

    :copyright: Copyright 2007-2018 by the Sphinx team, see README.
    :license: BSD, see LICENSE for details.
"""
from os import path


__version__ = '1.2.5'
__version_info__ = (1, 2, 5)

package_dir = path.abspath(path.dirname(__file__))

# must be imported last to avoid circular import
from sphinxcontrib.websupport.core import WebSupport  # NOQA
