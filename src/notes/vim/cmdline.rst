.. meta::
    :robots: noindex

Vim cmdline
===========

Range
-----

See ``:h [range]`` or ``:h cmdline-ranges``.

Range consists of one or more line specifiers, separated with ',' or ';'.

When separated with ';' the cursor position will be set to that line before
interpreting the next line specifier. This doesn't happen for ','.

The default line specifier for most commands is the cursor position, but the
ex commands ":write" and ":global" have the whole file (1,$) as default.

{number}
    an absolute line number

0
    The first line

1
    The first line

\.
    the current line

\$
    the last line in the file

\%
    equal to 1,$ (the entire file)

't
    position of mark t (lowercase)

'T
    position of mark T (uppercase); when the mark is in another file it cannot
    be used in a range

/{pattern}[/]
    the next of current line where {pattern} matches

?{pattern}[?]
    the previous of current line where {pattern} matches

\/
    the next line where the previously used search pattern matches

\?
    the previous line where the previously used search pattern matches

\&
    the next line where the previously used substitute pattern matches

Commands
--------

:[range]w[rite] [++opt] !{cmd}
    Execute {cmd} with [range] lines as standard input (note the space in front
    of the '!'). 

    The default [range] for the ":w" command is the whole buffer (1,$).
