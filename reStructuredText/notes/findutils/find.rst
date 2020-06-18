Findutils find
==============

List files greater (+) or smaller (-) than specified size: ::

    $ find <path> -size "+|-"<size>

Use all found files as a single argument of some command to execute: ::

    $ find <path> --exec <command> {} +

    Example:
    $ find /tmp/a --exec echo {} +
    /tmp/a /tmp/a/c /tmp/a/c/d /tmp/a/c/d/e /tmp/a/b /tmp/a/b/c

Use each found files as an argument appending to some command to execute
seperately: ::

    $ find <path> --exec <command> {} \;

    Example:
    $ find /tmp/a --exec echo {} \;
    /tmp/a
    /tmp/a/c
    /tmp/a/c/d
    /tmp/a/c/d/e
    /tmp/a/b
    /tmp/a/b/c

References
----------

``man find``
