# -*- coding: utf-8 -*-
"""setup.py"""

import os
import sys
from setuptools import setup
# from setuptools.command.test import test as TestCommand


def read_content(filepath):
    with open(filepath) as fobj:
        return fobj.read()


classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
]


long_description = ( 'long desc')

requires = ['setuptools', 'requests']

extras_require = {
    'reST': ['Sphinx'],
    }
if os.environ.get('READTHEDOCS', None):
    extras_require['reST'].append('recommonmark')

with open('requirements.txt', 'w') as _file:
    _file.write('\n'.join(requires))

with open('extras_requirement.txt', 'w') as _file:
    _file.write('\n'.join(extras_require.get('reST')))

setup(name='phonesimulator',
      version='0.1.0',
      description='##### ToDo: Rewrite me #####',
      long_description='my long desc',
      author='claudio',
      author_email='jcchauve@free.fr',
      url='https://github.com/jcchauve/phonesimulator',
      classifiers=classifiers,
      packages=['phonesimulator'],
      data_files=[],
      install_requires=requires,
      include_package_data=True,
      extras_require=extras_require,
      tests_require=['tox'],
      )
