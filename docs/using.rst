.. _usage:

====================
Using |project_name|
====================

First, you need to comply with the :ref:`requirements-to-use`.

Install |project_name| itself
=============================

To install |project_name| itself, you can simply use `pip` or, preferably, use `pipenv`.

If you choose `pipenv` as your recommended installation tool, you might need to install it first using

.. code-block:: shell

   $ pip install --user -U pipenv 

Then , simply use the following command:

.. code-block:: shell

   $ pipenv install invoke-sphinx

Integrate |project_name| in your project
========================================

To benefit from the tasks defined in |project_name| in your own project, you should create a ``tasks.py`` file at the root of your project, containing (at least):

.. code-block:: shell

   import invoke

   from invoke import task, Collection
   from invoke_sphinx import docs

   ns = Collection(docs)

.. note::

   Please refer to `the original invoke documentation <http://docs.pyinvoke.org/>`_ for more information about what can be achieved through this tool.

You also need to create an :file:`invoke.yml` file, at the root of your project, containing (at least):

.. code-block:: shell

   ---

   #######################################
   ###  Constants used to publish doc  ###
   #######################################

   ### remote doc server configuration
   # server host or IP
   remote_doc_server: '...'
   # username used to push documentation on the remote server
   remote_doc_server_username: '...'
   # password for the username used to push documentation on the remote server
   remote_doc_server_password: '...'
   # directory prefix in which the documentation is pushed (for example /var/www)
   remote_doc_server_path_prefix: '...'
   # project specific directory in which the documentation is pushed. 
   # this path is appended to the path_prefix above to define the directory in which the documentation is pushed
   # this path is also appended to the url used to expose your documentation (through the remote doc server)
   publishing_dir: '...'

These constants are used by tasks in |project_name| project to publish your documentation on the remote server.

.. note::

   You need, of course, to set values appropriate to your context.


Use |project_name| tasks
========================

Now that everything is ready, you can use ``invoke --list`` to see the list of tasks available.

.. note::

   If you have installed |project_name| with `pipenv` (which you should), you need to prefix your ``invoke`` commands with ``pipenv run ...`` or execute them in your virtualenv (see `pipenv documentation <https://pipenv.readthedocs.io/>`_ for more information on this matter.


For example, to generate your documentaton locally, use ``invoke docs.build``. This will compile your `*.rst` files into an html site, browsable from the `docs/_build/html` directory. The sources `rst` files are expected to be available in the `docs` directory.

For a detailed explanation of each task, see :doc:`tasks`.

.. note::

   The |project_name| project is using itself to handle its own documentation. Thus, it can serve as an example of how to integrate it into your own project.


Tips
====

Tab completion
--------------

You can benefit from tab completion with ``invoke`` commands.

To get it, you can add the following line in your ``~/.bash_aliases``:

.. code-block:: shell

   alias invoke-tab-completion="source <(invoke --print-completion-script bash)"

Then, simply execute ``invoke-tab-completion`` from the directory containing your ``tasks.py`` and start enjoying tab completion!

This will only impact your current shell. You need to do it each time you open a new shell. Also, when switching project, simply execute the command again to adapt the tab completion for your other commands.

If installed from `pipenv`, it is recommended to define the following aliases:

.. code-block:: shell

   alias vinvoke="pipenv run invoke"
   alias vinvoke-completion="source <(vinvoke --print-completion-script bash | sed -e 's/invoke/vinvoke/g')"


For the lazy ones
-----------------

``inv`` is an alias for ``invoke``. You can use ``inv docs.build`` instead of ``invoke docs.build`` for example : 3 characters gained !!

Still, the `pipenv run` thing still applies, so you could actually use ``pipenv run inv``.

