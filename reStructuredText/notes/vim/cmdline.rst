Vim cmdline
===========


{number}
    an absolute line number

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
    the next line where {pattern} matches

?{pattern}[?]
    the previous line where {pattern} matches

\/
    the next line where the previously used search pattern matches

\?
    the previous line where the previously used search pattern matches

\&
    the next line where the previously used substitute pattern matches

