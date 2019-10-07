import setuptools

NAME = "invoke-sphinx"
VERSION = "1.2.0"
REQUIRES = ['sphinx', 'sphinx_rtd_theme', 'sphinx-autobuild', 'sphinx-versions', 'invoke', 'pyyaml']

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=NAME,
    version=VERSION,
    author="Smile",
    author_email="cyrille.gachot@smile.fr",
    description="Invoke commands related to sphinx documentation",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/Smile-SA/' + NAME,
    packages=setuptools.find_packages(),
    install_requires=REQUIRES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

