Bash Redirection
================

Here documents
--------------

::

    [n]<<[-]word
        here-document
    delimiter

All of the lines read up to delimiter are then used as the standard input (or
file descriptor ``n`` if ``n`` is specified) for a command.

If word is quoted, the delimiter is the result of quote removal on word, and
the lines in the here-document are not expanded.

If word is unquoted, all lines of the here-document are subjected to *parameter
expansion*, *command substitution*, and *arithmetic expansion*, the character
sequence \<newline> is ignored, and \ must be used to quote the characters \,
$, and \`.

If the redirection operator is ``<<-``,  then all leading tab characters are
stripped from input lines and the line containing delimiter.


Here strings
------------

::

    [n]<<<word

The result is supplied as a single string, with a newline appended, to the
command on its standard input (or file descriptor ``n`` if ``n`` is specified).

The word undergoes *tilde expansion*, *parameter and variable expansion*,
*command substitution*, *arithmetic expansion*, and *quote removal*. Pathname
expansion and word splitting are not performed.
