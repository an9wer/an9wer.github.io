.. meta::
    :robots: noindex

Coreutils du
============

List all files and directories, not just directories (by default): ::

    # du -a <file> [<file> ...]

Scan only for specified depth: ::

    # du -d <depth> <file> [<file> ...]

Print only a total size of files (same as ``-d 0``): ::

    # du -s <file> [<file> ...]

Do not count size of subdirectories into directories: ::

    # du -S <file> [<file> ...]

Exclude files greater (-) or smaller (+) than specified size: ::

    # du -t "+|-"<size> <file> [<file> ...]

References
----------

``man du``
