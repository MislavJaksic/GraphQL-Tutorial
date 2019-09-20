GraphQL Tutorial
================

Install dependencies
--------------------

::

  $: pipenv install

Run GraphQL server
------------------

::

  $: pipenv run python src/example/runner.py
  # Note: visit localhost:5000 to browse the API though GraphiQL

Run tests
---------

::

  $: pipenv run pytest

Generate docs
-------------

::

  $: pipenv shell
  $: cd docs
  $: make html



Linter
------

::

  $: pipenv run flake8

Enter venv
----------

::

  $: pipenv shell
