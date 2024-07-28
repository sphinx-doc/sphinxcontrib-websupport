"""Test the Web Support Package search adapters."""

from __future__ import annotations

import importlib
from io import StringIO

import pytest

from sphinxcontrib.websupport import WebSupport

try:
    from sphinxcontrib.websupport.storage import sqlalchemy_db, sqlalchemystorage  # NoQA: F401
    sqlalchemy_missing = False
except ImportError:
    sqlalchemy_missing = True


skip_if_sqlalchemy_missing = pytest.mark.skipif(
    sqlalchemy_missing,
    reason='needs sqlalchemy',
)


def skip_unless_importable(module, msg=None):
    """Decorator to skip test if module is not importable."""
    try:
        importlib.import_module(module)
    except ImportError:
        return pytest.mark.skipif(True, reason=(msg or 'conditional skip'))
    else:
        return pytest.mark.skipif(False, reason=(msg or 'conditional skip'))


def search_adapter_helper(rootdir, tmp_path, adapter):
    support = WebSupport(
        srcdir=rootdir / 'test-searchadapters',
        builddir=tmp_path / 'websupport',
        status=StringIO(),
        warning=StringIO(),
        search=adapter,
    )
    support.build()

    s = support.search

    # Test the adapters query method. A search for "Epigraph" should return
    # one result.
    results = s.query('Epigraph')
    assert len(results) == 1, f'{adapter} search adapter returned {len(results)} search result(s), should have been 1'  # NoQA: E501

    # Make sure documents are properly updated by the search adapter.
    s.init_indexing(changed=['markup'])
    s.add_document('markup', 'filename', 'title', 'SomeLongRandomWord')
    s.finish_indexing()
    # Now a search for "Epigraph" should return zero results.
    results = s.query('Epigraph')
    assert len(results) == 0, f'{adapter} search adapter returned {len(results)} search result(s), should have been 0'  # NoQA: E501
    # A search for "SomeLongRandomWord" should return one result.
    results = s.query('SomeLongRandomWord')
    assert len(results) == 1, f'{adapter} search adapter returned {len(results)} search result(s), should have been 1'  # NoQA: E501
    # Make sure it works through the WebSupport API
    support.get_search_results('SomeLongRandomWord')


@skip_unless_importable('xapian', 'needs xapian bindings installed')
@skip_if_sqlalchemy_missing
def test_xapian(rootdir, tmp_path):
    search_adapter_helper(rootdir, tmp_path, 'xapian')


@skip_unless_importable('whoosh', 'needs whoosh package installed')
@skip_if_sqlalchemy_missing
def test_whoosh(rootdir, tmp_path):
    search_adapter_helper(rootdir, tmp_path, 'whoosh')
