Expansion
=========

Pathname expansion
------------------
**Note**: When in pathname matching context (pathname expansion), the slash
character must always be matched explicitly by a slash in the pattern, but in
other matching contexts (e.g. case statement, variable modification,
HISTIGNORE) it can be matched by a special pattern character.

Porcess substitution
--------------------

The form ``<(list)`` is used as an input file. We need to treat it as a file
when it is used as a command argument.

::

    $ cat <(echo 123)
    123

::

    $ echo <(echo 123)
    /dev/fd/63


The form ``>(list)`` is used as an output file:

::

    $ echo 123 > >(sed 's/123/321/')
    321

::

    $ echo 123 >(sed 's/123/321/')
    123 /dev/fd/63

References
""""""""""
https://www.tldp.org/LDP/abs/html/process-sub.html

