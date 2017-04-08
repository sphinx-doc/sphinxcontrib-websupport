# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import sphinxcontrib.websupport

long_desc = '''
sphinxcontrib-webuspport provides a Python API to easily integrate Sphinx
documentation into your Web application.
'''

requires = [
    'sqlalchemy>=0.9',
    'whoosh>=2.0',
]
extras_require = {
    # Environment Marker works for wheel 0.24 or later
    'test': [
        'pytest',
        'mock',  # it would be better for 'test:python_version in 2.7'
    ],
}


setup(
    name='sphinxcontrib-websupport',
    version=sphinxcontrib.websupport.__version__,
    url='http://sphinx-doc.org/',
    download_url='https://pypi.python.org/pypi/sphinxcontrib-websupport',
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requires,
    extras_require=extras_require,
    namespace_packages=['sphinxcontrib'],
)
