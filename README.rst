Blog
====

A statistics blog system inspired by `bashblog`_.

Features
--------

- posts written in `the reStructuredText markup language`_
- a build script written in `the Tcl programming language`_
- a simple HTTP server written in `the Tcl programming language`_
- support for generating an RSS feed
- support for generating a sitemap

Prerequisites
-------------

- Tcl >= 8.6
- `docutils`_ == 0.20.1

Usage
-----

Build all posts, the RSS feed file, and the sitemap file: ::

    $ ./build

Remove obsolete HTML files, after renaming post files: ::

    $ ./clean

Start a local HTTP server, listening on the port 8000: ::

    $ ./run

.. _bashblog: https://github.com/cfenollosa/bashblog
.. _the Tcl programming language: https://www.tcl.tk/
.. _the reStructuredText markup language: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
.. _docutils: https://docutils.sourceforge.io/
