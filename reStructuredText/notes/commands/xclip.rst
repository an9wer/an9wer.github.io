Xclip
=====

::

    xclip [OPTION] [FILE]...

Reads from standard in, or from one or more files, and makes the data available
as an X selection for pasting into X applications.

**Note** that only the first character of the selection specified with the
*-selection* option is important. This means that "p", "sec" and "clip" would
have the same  effect  as  using "primary", "secondary" or "clipboard"
respectively.


Examples
--------

Copy to clipboard:

::

    $ xclip -selection clipboard

Remove last newline character if existed and copy to clipboard:

::

    $ xclip -r -selection clipboard

Copy to clipboard and also print the text piped to standard:

::

    $ sclip -f -selection clipboard
    

Paste from clipboard:

::

    $ xclip -o -selection clipbard


    

