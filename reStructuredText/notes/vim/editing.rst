Vim Editing
===========

see *:h editing.txt*

CTRL-G | :f[ile]
    Prints the current file name

{count}CTRL-G
    Prints the current file name with full path. If the count is higher then 1,
    the current buffer number is also given.


Writing
-------

:[range]w[rite] [++opt] !{cmd}
    Execute {cmd} with [range] lines as standard input (note the space in front
    of the '!'). 



File encryption
---------------

See *:h encryption*

:X
    Prompt for an encryption key.  The typing is done without showing the
    actual text, so that someone looking at the display won't see it.

When you need to change encryption key, type ``:X`` again and save file, the
new key will work.


File searching
--------------

See *:h file-searching*

The file searching is currently used for the *path*, *cdpath* and *tags*
options, for `finddir()` and `findfile()`.  Other commands use `wildcards`
which is slightly different.

There are three different types of searching:

1.  Downward searching ('**', '*')
2.  Upward searching (';')
3.  Combined up/donwward searching ('**', '*', ';')
    
