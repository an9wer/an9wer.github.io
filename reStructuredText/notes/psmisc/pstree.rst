Pstree
======

`pstree` shows running processes as a tree. The tree is rooted at either pid or
init if pid is omitted. If a user name is specified, all process trees rooted
at processes owned by that user are shown.

::

    pstree [<options>] [pid|user]


Examples
--------

To show trees owned by specified user:

::

    $ pstree <user>

To show a tree start from specified process (pid):

::

    $ pstree <pid>


To show a tree of specified process, start from the most ancestor of that
specified process:

::

    $ pstree -s <pid>

To show a processes tree with pid of each process:

::

    $ pstree -p

To show a processes tree and highlight the current process and its ancestors.

::

    $ pstree -h

References
----------

See *man pstree*
