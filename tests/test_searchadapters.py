"""Test the Web Support Package search adapters."""

import shutil
from io import StringIO

import pytest

from sphinxcontrib.websupport import WebSupport

from test_websupport import skip_if_sqlalchemy_missing
from util import skip_unless_importable


def teardown_module(tmp_path):
    shutil.rmtree(tmp_path / 'websupport', ignore_errors=True)


@pytest.fixture
def search_adapter_helper(rootdir, tmp_path, adapter):
    support = WebSupport(
        srcdir=rootdir / 'test-searchadapters',
        builddir=tmp_path / 'websupport',
        status=StringIO(),
        warning=StringIO(),
        search=adapter
    )
    support.build()

    s = support.search

    # Test the adapters query method. A search for "Epigraph" should return
    # one result.
    results = s.query(u'Epigraph')
    assert len(results) == 1, \
        '%s search adapter returned %s search result(s), should have been 1'\
        % (adapter, len(results))

    # Make sure documents are properly updated by the search adapter.
    s.init_indexing(changed=['markup'])
    s.add_document(u'markup', u'filename', u'title', u'SomeLongRandomWord')
    s.finish_indexing()
    # Now a search for "Epigraph" should return zero results.
    results = s.query(u'Epigraph')
    assert len(results) == 0, \
        '%s search adapter returned %s search result(s), should have been 0'\
        % (adapter, len(results))
    # A search for "SomeLongRandomWord" should return one result.
    results = s.query(u'SomeLongRandomWord')
    assert len(results) == 1, \
        '%s search adapter returned %s search result(s), should have been 1'\
        % (adapter, len(results))
    # Make sure it works through the WebSupport API
    support.get_search_results(u'SomeLongRandomWord')


@skip_unless_importable('xapian', 'needs xapian bindings installed')
@skip_if_sqlalchemy_missing
def test_xapian(rootdir, tmp_path):
    search_adapter_helper(rootdir, tmp_path, 'xapian')


@skip_unless_importable('whoosh', 'needs whoosh package installed')
@skip_if_sqlalchemy_missing
def test_whoosh(rootdir, tmp_path, adapter):
    search_adapter_helper(rootdir, tmp_path, 'whoosh')
