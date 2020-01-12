# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

long_desc = '''
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.
'''

extras_require = {
    # Environment Marker works for wheel 0.24 or later
    'test': [
        'pytest',
        'sqlalchemy',
        'whoosh',
        'Sphinx',
    ],
    'lint': [
        'flake8',
    ],
}


def get_version():
    """Get version number of the package from version.py without importing core module."""
    package_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(package_dir, 'sphinxcontrib/websupport/version.py')

    namespace = {}
    with open(version_file, 'rt') as f:
        exec(f.read(), namespace)

    return namespace['__version__']


setup(
    name='sphinxcontrib-websupport',
    version=get_version(),
    url='http://sphinx-doc.org/',
    download_url='https://pypi.org/project/sphinxcontrib-websupport/',
    license='BSD',
    author='Georg Brandl',
    author_email='georg@python.org',
    description='Sphinx API for Web Apps',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    platforms='any',
    python_requires=">=3.5",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    extras_require=extras_require,
    entry_points={
        'sphinx.builders': [
            'websupport = sphinxcontrib.websupport.builder:WebSupportBuilder',
        ],
    },
    namespace_packages=['sphinxcontrib'],
)
