.. meta::
    :robots: noindex

Bash Expansion
==============

Parameter expansion
-------------------

${parameter:offset}  ${parameter:offset:length}
    Expands to up to *length* characters of the value of parameter starting at
    the character specified by *offset*. *length* and *offset* are arithmetic
    expressions.

    If *offset* evaluates to a number less than zero, the value is used as an
    *offset* in characters from the end of the value of parameter. If *length*
    evaluates to a number less than zero, it is interpreted as an *offset* in
    characters from the end of the value of parameter rather than a number of
    characters, and the expansion is the  characters between *offset* and that
    result. Note that a negative *offset* must be separated from the colon by
    at least one space to avoid being confused with the ``:-`` expansion.

${parameter/pattern/string}
    If parameter is @ or \*, the substitution operation is applied to each
    positional parameter in turn.

    If parameter is an array variable subscripted with @ or \*, the
    substitution  operation  is  applied to each member of the array in turn.

    The pattern is expanded to produce a pattern just as in pathname expansion.

    Normally only the first match is replaced.

    If pattern begins with /, all matches of pattern are replaced with string. 

    If pattern begins with #, it must match at the beginning of the expanded
    value of parameter.

    If pattern begins with %, it must match at the end of the expanded value of
    parameter.

Pathname expansion
------------------

**Note**: When in pathname matching context (pathname expansion), the slash
character must always be matched explicitly by a slash in the pattern, but in
other matching contexts (e.g. case statement, variable modification,
HISTIGNORE) it can be matched by a special pattern character.

\*
    Matches any string, including the null string.

\?
    Matches any single character.

[...]
    Matches any one of the enclosed characters.


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

The  shell treats each character of **IFS** as a delimiter, and splits the
results of the other expansions into words using these characters as field
terminators.

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
----------

https://www.tldp.org/LDP/abs/html/process-sub.html

