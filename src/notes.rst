.. meta::
    :robots: noindex 

Commands/
    -   `less </notes/commands/less.html>`_ - opposite of more
    -   `info </notes/commands/info.html>`_ - read info documents
    -   `sed </notes/commands/sed.html>`_ - stream editor for filtering and transforming text

Q: How to find largest file in directory recursively?

A: ::

    # find / -type f -exec du -ha {} + | sort -rh
