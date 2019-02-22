=============
Tasks details
=============

Please refer to the documentation on :ref:`usage` for a discussion on ``invoke`` vs ``vinvoke`` vs ``pipenv run invoke``.

Clean
=====

.. _doc-clean:

docs.clean
----------

.. code-block:: shell

   $ invoke docs.clean

This will clean the `docs/_build` directory to ensure fresh documentation (especially in case of file removal).

*Implementation note:* ``docs.clean`` is the equivalent of the `Sphinx` command:

.. code-block:: shell

   $ make -C docs clean


Open
====

docs.open
---------

.. code-block:: shell

   $ invoke docs.open [--local]

This will open your browser at your documentation url, on the remote server. If ``--local`` or ``-l`` flag is passed, the local documentation is opened instead.

This does not (re)build your documentation, so if the ``--local`` flag is used, you need to :ref:`build <doc-build>` your documentation locally first.

*Implementation note:* ``docs.open`` delegates to ``xdp-open`` command.


Test
====

docs.test
---------

.. code-block:: shell

   $ invoke docs.test

This will test the links in your documentation, and report potential issues. This is usefull to ensure your documentation is coherent, both for internal and external links.

*Implementation note:* ``docs.test`` is the equivalent of the `Sphinx` command:

.. code-block:: shell

   $ make -C docs linkcheck


Build
=====

.. _doc-build:

docs.build
----------

.. code-block:: shell

   $ invoke docs.build

This will generate the HTML documentation in the `docs/_build/html` directory. You can visualize it by browsing your navigator to this directory.

It will always call the :ref:`doc-clean` task first.

*Implementation note:* ``docs.build`` is the equivalent of the `Sphinx` command:

.. code-block:: shell

   $ make -C docs html


.. _doc-build-versions:

docs.build-versions
-------------------

.. code-block:: shell

   $ invoke docs.build-versions

This will generate the HTML documentation in the `docs/_build/html` directory, for all your project versions. You can visualize it by browsing your navigator to this directory.

.. note::

   In this case, the documentation generation is done through what is available in the git repository. Local changes are not taken into account.

It will always call the :ref:`doc-clean` task first.

*Implementation note:* ``docs.build-versions`` is the equivalent of the `Sphinx` command:

.. code-block:: shell

   $ sphinx-versioning build docs docs/_build/html

where ``build`` is the command, ``docs`` the directory containing your documentation, and ``docs/_build/html`` the target directory.


docs.build-pdf
--------------

.. code-block:: shell

   $ invoke docs.build-pdf

This will generate the PDF documentation in the `docs/_build/latex` directory. You can visualize it by browsing your file explorer to this directory.

It will always call the :ref:`doc-clean` task first.

.. note:: 

   You might need to install latex on your local computer first. See :ref:`install-latex` for more information.

*Implementation note:* ``docs.build-pdf`` is the equivalent of the `Sphinx` command:

.. code-block:: shell

   $ make -C docs latexpdf


Live Build
==========

docs.live
---------

.. code-block:: shell

   $ invoke docs.live

This will scan your documentation and build it everytime you change a file. It will also open a brower poiting to your local documentation. It includes a live-reload server, which reloads your current page if it changes.

This is particularly usefull if you are currently updating your documentation, to see changes in real-time.

.. note::

   This is the default task of the `docs` module, meaning you can simply use ``invoke docs`` to call this task.

*Implementation note:* ``docs.live`` is the equivalent of the `sphinx-autobuild` command:

.. code-block:: shell

   $ sphinx-autobuild -B --delay 1 -b html docs docs/_build/html

... with some files being ignored as well.

Publish
=======

Documentation is published on the remote server defined in the configuration file :file:`invoke.yml`.

.. _doc-publish:

docs.publish
------------

.. code-block:: shell

   $ invoke docs.publish

This will rsync the `docs/_build/html` directory to the remote server.

It will always call the :ref:`doc-build` task first.

*Implementation note:* ``docs.publish`` is the equivalent of the command:

.. code-block:: shell

   $ rsync -r -P -e ssh docs/_build/html/ ${remote_doc_server_username}@${remote_doc_server}:${remote_doc_server_path_prefix}/${publishing_dir}/


docs.publish-versions
---------------------

.. code-block:: shell

   $ invoke docs.publish-versions

This will rsync the `docs/_build/html` directory to the remote server. It is the same command as :ref:`doc-publish`, the difference being the generation task called first.

It will always call the :ref:`doc-build-versions` task first.


