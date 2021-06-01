.. meta::
    :robots: noindex

Coreutils head
==============

Print the first NUM lines, with the leading '-', print all but the last NUM
lines: ::

    $ head -n <NUM> <file> [<file> ...]

    e.g.
    $ head -n  1 /var/log/pacman.log
    $ head -n -1 /var/log/pacman.log

References
----------

``man head``
