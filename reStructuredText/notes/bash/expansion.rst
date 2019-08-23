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


Word splitting
--------------

The shell scans the results of *parameter expansion*, *command substitution*,
and *arithmetic expansion* that did not occur within double quotes for word
splitting.

**Note** that if no expansion occurs, no splitting is performed.

::

    $ a="1     2   3"
    $ func() { echo ${#@}; }

    $ func $a       # Word splitting is performed
    3

    $ func "$a"     # Word splitting is not performed
    1

    $ func "1     2   3"    # Word splitting is not performed
    1

    $ func 1     2   3      # Word splitting is not performed
    3


References
""""""""""
https://www.tldp.org/LDP/abs/html/process-sub.html

