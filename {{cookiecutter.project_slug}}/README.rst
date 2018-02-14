.. image:: https://travis-ci.org/{{cookiecutter.project_org}}/{{cookiecutter.project_name}}.svg?branch=master
    :target: https://travis-ci.org/{{cookiecutter.project_org}}/{{cookiecutter.project_name}}
.. image:: https://anaconda.org/{{cookiecutter.project_org}}/{{cookiecutter.project_name}}/badges/version.svg
    :target: https://anaconda.org/{{cookiecutter.project_org}}/{{cookiecutter.project_name}}
.. image:: https://codecov.io/gh/{{cookiecutter.project_org}}/{{cookiecutter.project_name}}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{cookiecutter.project_org}}/{{cookiecutter.project_name}}

*Put a general description of the project here*

Installation
============

{{cookiecutter.project_name}} can be installed with pip (system wide or in a virtual environment):

.. code:: bash

    pip install {{cookiecutter.project_slug}}

Alternatively, you can install {{cookiecutter.project_name}} in your home directory:

.. code:: bash

    pip install {{cookiecutter.project_slug}} --user

Lastly, you can also install {{cookiecutter.project_name}} with conda. (See
https://www.continuum.io/downloads)

.. code:: bash

    conda install -c {{cookiecutter.project_org}} {{cookiecutter.project_slug}}


Testing
=======

The tests can be executed as follows:

.. code:: bash

    nosetests {{cookiecutter.project_slug}}


Background and usage
====================

*Put some more details here*

Release history
===============

- {% now 'local', '**%Y-%d-%m**' %} 0.0.0

  Initial Release


How to make a release (Github, PyPI and anaconda.org)
=====================================================

Before you do this, make sure everything is OK. The PyPI releases cannot be undone. If you
delete a file from PyPI (because of a mistake), you cannot upload the fixed file with the
same filename! See https://github.com/pypa/packaging-problems/issues/74

1. Update the release history.
2. Commit the final changes to master and push to github.
3. Wait for the CI tests to pass. Check if the README looks ok, etc. If needed, fix things
   and repeat step 2.
4. Make a git version tag: ``git tag <some_new_version>`` Follow the semantic versioning
   guidelines: http://semver.org
5. Push the tag to github: ``git push origin master --tags``
