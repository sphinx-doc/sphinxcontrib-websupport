# -*- coding: utf-8 -*-
"""
    sphinxcontrib.websupport.utils
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2007-2016 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from docutils import nodes


def is_commentable(node: nodes.Node) -> bool:
    # return node.__class__.__name__ in ('paragraph', 'literal_block')
    return node.__class__.__name__ == 'paragraph'
