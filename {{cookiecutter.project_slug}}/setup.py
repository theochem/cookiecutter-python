#!/usr/bin/env python
# -*- coding: utf-8 -*-
# {{cookiecutter.description}} 
# Copyright (C) {% now 'local', '%Y' %} {{cookiecutter.author}} <{{cookiecutter.email}}>
#
# This file is part of {{cookiecutter.project_name}}.
#
# {{cookiecutter.project_name}} is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# {{cookiecutter.project_name}} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
# --
"""{{cookiecutter.project_name}} setup script.

If you are not familiar with setup.py, just use pip instead:

    pip install {{cookiecutter.project_name}} --user --upgrade

Alternatively, you can install from source with

    ./setup.py install --user
"""

from __future__ import print_function

from setuptools import setup

def get_version():
    """Load the version from version.py, without importing it.

    This function assumes that the last line in the file contains a variable defining the
    version string with single quotes.

    """
    with open('{{cookiecutter.project_name}}/version.py', 'r') as f:
        return f.read().split('=')[-1].replace('\'', '').strip()


def readme():
    """Load README.rst for display on PyPI."""
    with open('README.rst') as f:
        return f.read()


setup(
    name='{{cookiecutter.project_name}}',
    version=get_version(),
    description='{{cookiecutter.description}}',
    long_description=readme(),
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    url='https://github.com/{{cookiecutter.project_org}}/{{cookiecutter.project_name}}',
    packages=['{{cookiecutter.project_name}}'],
    zip_safe=False,
)
