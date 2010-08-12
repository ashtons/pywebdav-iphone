#!/usr/bin/env python

try: 
   from ez_setup import use_setuptools 
   use_setuptools() 
except ImportError: 
   pass 

from setuptools import setup

VERSION = open('VERSION', 'r').read()
VERSION = VERSION.replace('\n', '')

CHANGES = open('doc/Changes', 'r').read()

DOC = """
WebDAV library for python. 

Consists of a *server* that is ready to run
Serve and the DAV package that provides WebDAV server(!) functionality.

Currently supports 

    * WebDAV level 1
    * Level 2 (LOCK, UNLOCK)
    * Experimental iterator support

It plays nice with

    * Mac OS X Finder
    * Windows Explorer
    * iCal
    * cadaver
    * Nautilus

This package does *not* provide client functionality.

Installation
============

After installation of this package you will have a new script in you $PYTHON/bin directory called
*davserver*. This serves as the main entry point to the server.

Examples
========

Example (using easy_install)::

    easy_install PyWebDAV
    davserver -D /tmp -n

Example (unpacking file locally)::

    tar xvzf PyWebDAV-$VERSION.tar.gz
    cd pywebdav
    python setup.py develop
    davserver -D /tmp -n

For more information: http://code.google.com/p/pywebdav/

Changes
=======

%s
""" % CHANGES

from distutils.core import setup
setup(name='PyWebDAV',
      description='WebDAV library including a standalone server for python',
      author='Simon Pamies',
      author_email='spamsch@gmail.com',
      maintainer='Simon Pamies',
      maintainer_email='spamsch@gmail.com',
      url='http://code.google.com/p/pywebdav/',
      platforms=['Unix', 'Windows'],
      license='GPL v2',
      version=VERSION,
      long_description=DOC,
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries'
          ],
      keywords = ['webdav',
                  'server',
                  'dav',
                  'standalone',
                  'library',
                  'gpl',
                  'http',
                  'rfc2518',
                  'rfc 2518'],
      packages=['DAV', 'DAVServer'],
      zip_safe=False,
      entry_points={
          'console_scripts' : ['davserver = DAVServer.server:run']
      }
      )
