import invoke
import os


from invoke import task, Collection

ns = Collection("docs")
###############################################################################
###                              CONFIGURATION                              ###
###############################################################################

##### Configuration
default_docs_directory = "docs"

def doc_build_directory(docs_directory):
    return "{}/_build/html/".format(docs_directory)

def remote_doc_target_directory(c):
    return "{}/{}/".format(c.remote_doc_server_path_prefix, c.publishing_dir)

def remote_doc_url(c):
    return "http://{}/{}".format(c.remote_doc_server, c.publishing_dir)

##### Common constants
help_docs_directory = "Directory containing the source documentation (default="+default_docs_directory+")."


###############################################################################
###                           DOCUMENTATION TASKS                           ###
###############################################################################

##### Common functions

def run_sphinx(c, docs_directory, command):
    return c.run("make -C {} {}".format(docs_directory, command))

def run_rsync_doc(c, docs_directory):
    directory = remote_doc_target_directory(c)
    server = c.remote_doc_server
    r = c.run("ssh {}@{} \"mkdir -p {}\"".format(c.remote_doc_server_username, server, directory))
    if not r:
        print("Unable to create remote directory {} on server {}".format(directory, server))
        return r
    r = c.run("rsync -q -r --delete -P -e ssh {} {}@{}:{}".format(
       doc_build_directory(docs_directory),
       c.remote_doc_server_username,
       c.remote_doc_server,
       remote_doc_target_directory(c)
    ))
    if not r:
        print("Unable to synchronize the remote directory {} on server {}".format(directory, server))
        return r
    print("Done - Your documentation is available at {}".format(remote_doc_url(c)))
    return r


##### Opening

@task(help={'docs-directory': help_docs_directory, 'local': 'Flag to open the local doc instead of the remote one'})
def doc_open(c, docs_directory=default_docs_directory, local=False):
    """
    Open a browser on your documentation
    """
    open_prg = "/usr/bin/xdg-open"
    doc_path = doc_build_directory(docs_directory)+'index.html' if local else remote_doc_url(c)
    if os.path.exists(open_prg):
        r = c.run(open_prg + ' ' + doc_path)
        if not r:
            print("Unable to open you documentation. You can manually browse to {}".format(doc_path))
    else:
        print("Missing {} executable. Will not open the documentation. You can manually browse to {}".format(
            open_prg,
            doc_path,
        ))

ns.add_task(doc_open, 'open')


##### Cleaning

@task(help={'docs-directory': help_docs_directory})
def doc_clean(c, docs_directory=default_docs_directory):
    """
    Clean local documentation
    """
    print("\n\n##### Cleaning local documentation #####\n")
    run_sphinx(c, docs_directory, "clean")

ns.add_task(doc_clean, 'clean')


##### Testing

@task(help={'docs-directory': help_docs_directory})
def doc_test(c, docs_directory=default_docs_directory):
    """
    Test the links in your documentation
    """
    print("\n\n##### Testing local documentation #####\n")
    run_sphinx(c, docs_directory, "linkcheck")

ns.add_task(doc_test, "test")


##### Generation

@task(pre=[doc_clean], help={'docs-directory': help_docs_directory, 'open': 'Flag to open the local doc once built'})
def doc_generate(c, docs_directory=default_docs_directory, open_=False):
    """
    Build locally the documentation
    """
    print("\n\n##### Building local documentation #####\n")
    run_sphinx(c, docs_directory, "html")
    if open_:
        doc_open(c, docs_directory, True)

ns.add_task(doc_generate, 'build')

@task(
  pre=[doc_clean],
  help={
    'docs-directory': help_docs_directory,
    'pdf': 'Flag to also generate PDF versions (True by default)',
    'open': 'Flag to open the local doc once built (False by default)'
  }
)
def doc_generate_versions(c, docs_directory=default_docs_directory, pdf=True, open_=False):
    """
    Build locally the documentation, for all versions
    """
    print("\n\n##### Building local documentation, for all versions #####\n")
    pdf_option=""
    if pdf:
        pdf_option=" -P {}.pdf".format(c.project)
    c.run("sphinx-versioning build{} {} {}".format(pdf_option, docs_directory, doc_build_directory(docs_directory)))
    if open_:
        doc_open(c, docs_directory, True)

ns.add_task(doc_generate_versions, 'build-versions')

@task(pre=[doc_clean], help={'docs-directory': help_docs_directory})
def doc_pdf(c, docs_directory=default_docs_directory):
    """
    Build locally the documentation, in PDF format (through latex)
    """
    print("\n\n##### Building local documentation, in PDF format #####\n")
    run_sphinx(c, docs_directory, "latexpdf")

ns.add_task(doc_pdf, 'build-pdf')

##### Publishing

@task(default=True, pre=[doc_clean], help={'docs-directory': help_docs_directory})
def doc_livehtml(c, docs_directory=default_docs_directory):
    """
    Live build of documentation on each modification. 
    Open a browser with a local server to serve documentation.
    Opened page is reloaded each time documentation is generated.
    """
    print("\n\n##### Auto-Building local documentation #####\n")
    command = ' '.join([
        'sphinx-autobuild',
        '-B',
        '--delay 1',
        '--ignore "*.swp"',
        '--ignore "*.log"',
        '--ignore "*~"',
        '-b html',
        docs_directory,
        doc_build_directory(docs_directory)
    ])
    c.run(command)

ns.add_task(doc_livehtml, 'live')


@task(pre=[doc_generate], help={'docs-directory': help_docs_directory, 'open': 'Flag to open the local doc once built'})
def doc_publish(c, docs_directory=default_docs_directory, open_=False):
    """
    Publish the documentation on documentation server
    """
    print("\n\n##### Publishing documentation #####\n")
    run_rsync_doc(c, docs_directory)
    if open_:
        doc_open(c, docs_directory)

ns.add_task(doc_publish, 'publish')

@task(
    help={
        'docs-directory': help_docs_directory,
        'pdf': 'Flag to also generate PDF versions (True by default)',
        'open': 'Flag to open the local doc once built'
    }
)
def doc_publish_versions(c, docs_directory=default_docs_directory, pdf=True, open_=False):
    """
    Publish the documentation on documentation server, for all versions
    """
    doc_generate_versions(c, docs_directory, pdf, open_)

    print("\n\n##### Publishing documentation, for all versions #####\n")
    run_rsync_doc(c, docs_directory)
    if open_:
        doc_open(c, docs_directory)

ns.add_task(doc_publish_versions, 'publish-versions')

