"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
# To use a consistent encoding
from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        tox.cmdline(args=args)

# Get the long description from the README.md file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get version from the VERSION file
with open(path.join(here, 'morelia/VERSION'), encoding='utf-8') as f:
    version = f.readline().strip()

setup(
    name='morelia',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='Morelia is a AI (bot) for Slack!',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/ghostsquad/morelia.git',

    # Author details
    author='Weston McNamee',
    author_email='ghost.squadron@gmail.com',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Private :: Do Not Upload',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='slack bot ai python',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'PyYAML>=3.11',
        'slacker>=0.9.25',
        'websocket-client>=0.37.0',
        'pycontracts'
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': ['pytest==2.9.2',
                 'pytest-cov',
                 'pytest-html',
                 'tox==2.3.1',
                 'assertpy',
                 'mock',
                 'requests-mock==1.0.0']
    },

    cmdclass={'test': Tox},
)
