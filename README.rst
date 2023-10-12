Blog
====

My personal statistics blog system.

Features
--------

- buld scripts written in the `Tcl`_ programming language
- posts written in the `reStructuredText`_ markup language
- support for generating an RSS feed
- support for generating a sitemap

Prerequisites
-------------

- Tcl >= 8.5
- `docutils`_

Usage
-----

Build all posts, the RSS feed file, and the sitemap file: ::

    $ ./build

Remove obsolete HTML files, after renaming post files: ::

    $ ./clean

Start a local web server, and open the home page on Firefox: ::

    $ ./run

.. _Tcl: https://www.tcl.tk/
.. _reStructuredText: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
.. _docutils: https://docutils.sourceforge.io/
