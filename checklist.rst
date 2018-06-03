ToDo for releasing
=====================

1. check travis-ci testing result
2. check release version in ``sphinxcontrib/websupport/version.py`` and ``CHANGES``
3. build distribtion files: ``python setup.py release sdist bdist_wheel``
4. make a release: ``twine upload --sign --identity=<your-identify> dist/<new-version-files>``
5. check PyPI page: https://pypi.org/p/sphinxcontrib-websupport
6. tagging with version name. e.g.: git tag 1.1.0
7. bump version in ``sphinxcontrib/websupport/version.py`` and ``CHANGES``

