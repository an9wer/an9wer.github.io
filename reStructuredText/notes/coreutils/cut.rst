.. meta::
    :robots: noindex

Coureutils cut
--------------

In following command, *LIST* is made up of one range, or many ranges separated
by commas. Selected input is written in the same order that it is read, and is
written exactly once. Each range is one of:

-   N: N'th byte, character or field, counted from 1

-   N-: from N'th byte, character or field, to end of line

-   N-M: from N'th to M'th (included) byte, character or field

-   -M: from first to M'th (included) byte, character or field


Select bytes:

::

    $ echo -e '123456\nabcdef' | cut -b 1,3
    13
    ac

Select characters:

::

    $ echo -e '123456\nabcdef' | cut -c 2-4
    234
    bcd

Select fields delimited by TAB (default):

::

    $ echo -e '123\t456\nabc\tdef' | cut -f 1
    123
    abc

Select fields delimited by white spece:

::

    $ echo -e '123 456\nabc def' | cut -d ' ' -f 1
    123
    abc

**Note**: The delimiter accept only one single character.

Select fields delimited by which space but do not print lines not containing
delimiters:

::

    $ echo -e '123 456\nabcdef' | cut -d ' ' -f 1 -s
    123

Complement the set of selected bytes, characters or fields (more like reverse):

::

    $ echo -e '123 456\nabc def' | cut -d ' ' -f 1 --complement
    456
    def

Replace delimiter:

::

    $ echo -e '1   2   3' | cut -d ' ' -f 1- --output-delimiter=a
    1aaa2aaa3

