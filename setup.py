#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'onshape',
    'version': '1.0.0',
    'description': 'Sample package to demonstrate using Onshape API keys',
    'long_description': open('README.md').read(),
    'author': 'Ty-Lucas Kelley',
    'url': 'https://github.com/onshape/onshape/tree/master/python',
    'license': open('LICENSE').read(),
    'packages': [
        'onshape'
    ],
    'install_requires': ['requests'],
    'classifiers': [
        'Programming Language :: Python',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
}

setup(**config)
