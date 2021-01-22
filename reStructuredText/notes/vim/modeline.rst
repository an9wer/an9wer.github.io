Vim modline
===========

There are two forms of modelines.

Form 1: ::

    [text]{white}{vi:|vim:|ex:}[white]{options}

The *options* in this modeline are seperated with white space or ':', where
each part between ':' is the argument for a ":set" command.

Form 2: ::

    [text]{white}{vi:|vim:|Vim:|ex:}[white]se[t] {options}:[text]

The *option* in this modeline are seperated with white space, which is the
argument for a ":set" command.

**Note**: If you want to include a ':' in a set command precede it with a '\\'.
The backslash in front of the ':' will be removed.

::

    /* vi:set dir=c\:\tmp: */

This sets the 'dir' option to "c:\\tmp". Only a single backslash before the ':'
is removed.  Thus to include "\\:" you have to specify "\\\\:".
