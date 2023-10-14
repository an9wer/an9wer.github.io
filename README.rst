Blog
====

My personal statistics blog system.

Features
--------

- buld scripts written in `the Tcl programming language`_
- posts written in `the reStructuredText markup language`_
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

Start a local web server, and open the home page on Firefox: ::

    $ ./run

.. _the Tcl programming language: https://www.tcl.tk/
.. _the reStructuredText markup language: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
.. _docutils: https://docutils.sourceforge.io/
