.. _requirements-to-use:

==================
Usage Requirements
==================

.. _install-python:

Install Python & PIP & pipenv
=============================

First, you need to install Python 3 and PIP (if not already present on your system):

.. code-block:: shell

   $ sudo apt-get install python3-pip

You might need to update PIP right away

.. code-block:: shell

   $ pip3 install -U pip


.. _install-latex:

Install Latex
=============

To install Latex on your local computer, simply install the required packages through apt:

.. code-block:: shell

   $ sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk 

`latex` will be used if you want to generate PDF versions of the documentation.


Install other usefull stuff
===========================

Depending on your currently installed packages, you might also need:

.. code-block:: shell

   $ sudo apt-get install rsync


Now you're all set. If you only want to **use** the `invoke-sphinx` project, you can move on to the next page. If you are planning on contributing to the project, see :ref:`requirements-to-contribute`.

