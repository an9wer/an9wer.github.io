Regex
=====

`GNU regex <https://www.regular-expressions.info/gnu.html>`_

Regex engine
------------

There are basically only two kinds of regular expression engines: text-directed
engines(**DFA**), and regex-directed engines (**NFA**). Nearly all modern regex
flavors are based on regex-directed engines.

-   A regex-directed engine walks through the regex, attempting to match the
    next token in the regex to the next character. If a match is found, the
    engine advances through the regex and the subject string. If a token fails
    to match, the engine backtracks to a previous position in the regex and the
    subject string where it can try a different path through the regex.

-   A text-directed engine walks through the subject string, attempting all
    permutations of the regex before advancing to the next character in the
    string.  A text-directed engine never backtracks.

References
""""""""""

-   https://www.regular-expressions.info/engine.html

-   https://se.ifmo.ru/~ad/Documentation/Mastering_RegExp/mastregex2-CHP-4-SECT-3.html

Attributes of regex-directed engine
-----------------------------------

Eager
    It will stop searching as soon as it finds a valid match.

Backtracking
    Backtrack to a previous position in the regex if match fails.

Backtracking in NFA
-------------------

::

    $ echo "abc 123d" | sed -E 's/.*([0-9]+)/\1/'
    3d

-   https://www.regular-expressions.info/repeat.html
