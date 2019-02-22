=================
How to contribute
=================

First you need to ensure to meet the :ref:`requirements-to-contribute`.

Build and upload a new version of |project_name| 
================================================

Update the version of |project_name|
------------------------------------

You need to update two different files :

* ``setup.py``: contains the `VERSION` constant, used to identify the version built and uploaded to PyPI.
* ``invoke.yml``: contains the `version` constant, used to identify the version in the documentation.

Generate package to distribute
------------------------------

This creates the `dist` directory (among other things).

.. code:: bash

   python3 setup.py sdist bdist_wheel

Upload your package
-------------------

.. code:: bash

   twine upload dist/*


