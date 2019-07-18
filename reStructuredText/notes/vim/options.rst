Options
=======

paste
    Put vim in paste mode. This will avoid unexpected effects when pasting text
    in insert mode.

lhsearch


shortmess

regexpengine


modeline
    If starting editing a new file, and the 'modeline' option is on, a number
    of lines at the beginning and end of the file are checked for modelines.
    
Modline
-------

There are two forms of modelines.

::

    [text]{white}{vi:|vim:|ex:}[white]{options}

The *options* in this modeline are seperated with white space or ':', where
each part between ':' is the argument for a ":set" command.

::

    [text]{white}{vi:|vim:|Vim:|ex:}[white]se[t] {options}:[text]

The *option* in this modeline are seperated with white space, which is the
argument for a ":set" command.

**Note**: If you want to include a ':' in a set command precede it with a '\\'.
The backslash in front of the ':' will be removed.

::

    /* vi:set dir=c\:\tmp: */

This sets the 'dir' option to "c:\\tmp". Only a single backslash before the ':'
is removed.  Thus to include "\\:" you have to specify "\\\\:".

