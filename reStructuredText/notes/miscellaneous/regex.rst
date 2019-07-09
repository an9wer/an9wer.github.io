Regex
=====

`GNU regex <https://www.regular-expressions.info/gnu.html>`_

Regex engine
------------

There are basically only two kinds of regular expression engines: text-directed
engines, and regex-directed engines (NFA). Nearly all modern regex (DFA)
flavors are based on **regex-directed engines (NFA)**. 

Regex engine is eager, this means it will stop searching as soon as it finds a
valid match.

References
""""""""""

-   https://www.regular-expressions.info/engine.html

-   https://se.ifmo.ru/~ad/Documentation/Mastering_RegExp/mastregex2-CHP-4-SECT-3.html


Backtracking in NFA
-------------------

::

    $ echo "abc 123d" | sed -E 's/.*([0-9]+)/\1/'
    3d

-   https://www.regular-expressions.info/repeat.html


