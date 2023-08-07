"""The default search adapter, does nothing."""

from sphinxcontrib.websupport.search import BaseSearch
from sphinxcontrib.websupport.errors import NullSearchException


class NullSearch(BaseSearch):
    """A search adapter that does nothing. Used when no search adapter
    is specified.
    """
    def feed(self, pagename, filename, title, doctree):
        pass

    def query(self, q):
        raise NullSearchException('No search adapter specified.')
