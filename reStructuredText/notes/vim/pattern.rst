Vim Pattern
===========

See ``:h pattern.txt``.

g*
    Search forward for the word nearest to the cursor, like "*", but don't put
    "\<" and "\>" around the word.

g#
    Search backword for the word nearst to the cursor, like "#", but don't put
    "\<" and "\>" around the word.


A pattern contains one or more branches (multiple branched are seperated by
"\|"). (see ``:h /pattern``)

a branch contains one or more contacts (multiple contacts are seperated by
"\&"). (see ``:h /branch``)

A concat is one or more pieces, concatenated. (see ``:h /contact``)

A piece is an atom, possibly followed by a multi, an indication of how many
times the atom can be matched. Example: "a*" matches any sequence of "a". (see
``:h /piece``)

An atom can be one of a long list of items (use "\(" to group pattern into an
atom). Many atoms match one character in the text. It is often an ordinary
character or a character class. (see ``:h /atom``)

To clear last used search pattern:

::

    :set @/= ""

Magic
-----

\\m
    magic mode.

\\M
    nomagic mode.

\\v
    very magic mode, means that after it, all ASCII characters except '0'-'9',
    'a'-'z', 'A'-'Z' and '_' have special meaning.

\\V
    very nomagic mode, means that after it, only a backslash and terminating
    character (usually / or ?) have special meaning.
