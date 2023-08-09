from pathlib import Path

import pytest

import sphinx

pytest_plugins = 'sphinx.testing.fixtures'


@pytest.fixture(scope='session')
def rootdir():
    if sphinx.version_info[:2] < (7, 2):
        from sphinx.testing.path import path

        return path(__file__).parent.abspath() / 'roots'

    return Path(__file__).resolve().parent / 'roots'
