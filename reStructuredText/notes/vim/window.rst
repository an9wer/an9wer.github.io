Vim Window
==========

See ``:h windows.txt``

Buffer
------

- A buffer is the in-memory text of a file.
- A window is a viewport on a buffer.
- A tab page is a collection of windows.

A window is a viewport onto a buffer. You can use multiple windows on one
buffer, or several windows on different buffers.

A buffer is a file loaded into memory for editing. The original file remains
unchanged until you write the buffer to the file.



Moving cursor
-------------

CTRL-W p | CTRL-W CTRL-P
    Go to previous (last accessed) window (or switch between windows)


Window resize
-------------

See ``:h window-resize``

:resize [+|-][N]
    Resize current window height (default: hightest possible)

:vertical resize [+|-][N]
    Resize current window width (default: widest possible)

