GraphQL Tutorial
================

docs
----

::

  $: pipenv shell
  $: cd docs
  $: make html

src
---

::

  $: pipenv --python Python-Version

::

  $: pipenv run python ./src/big_package/runner.py
  $: pipenv run

tests
-----

::

  $: pipenv run pytest


Pipfile/Pipfile.lock
--------------------

Dependencies and the virtual environment are managed by pipenv.

::

  $: pipenv install
  $: pipenv install Package-Name==Package-Version

README.rst
----------

Why reStructuredText and not Markdown?
PyPI cannot display Markdown, but both GitHub and PyPI can display reStructuredText.

setup.cfg
---------

Configure flake8.

setup.py
--------

Define entry point, required packages and metadata.



Linter
------

::

  $: pipenv run flake8

Enter venv
----------

::

  $: pipenv shell
