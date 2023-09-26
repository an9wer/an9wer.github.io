Blog
====

My personal statistics blog system.

Prerequisites
-------------

All posts are written in the reStructuredText (RST) markup language, and I am
using `docutils <https://docutils.sourceforge.io/>`_ to convert them into HTML
files, which can be installed as: ::

    $ pip install docutils

Usage
-----

Build all posts and generate a RSS subscription as well: ::

    $ ./build

Remove obsolete HTML files (e.g. if renaming the name of RST files): ::

    $ ./clean

Run a simple web server (Python's http.server) locally and review posts on
Firefox: ::

    $ ./run
