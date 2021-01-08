Emerge
======

Use emerge via http proxy: ::

    # export http_proxy=http://<ip>:<port>

Update repositories: ::

    1.
    # emerge --sync [<repo>|<alias> ...]

    e.g.
    # emerge --sync
    # emerge --sync an9wer

    2.
    # emaint [-r <repo>] sync

    e.g.
    # emaint sync
    # emaint -r an9wer sync

    3.
    # emerge-webrsync
    
    Note: The emerge-webrsync program will download the entire ebuild
    repository as a tarball, which is much faster than emerge --sync for first
    time syncs.

Search match packages, which support a regular expression search by prefixing
the search string with ``%``: ::

    # emerge -s <package>

    e.g.
    # emerge -s cpupower
    # emerge -s "%^kde"

Remove package from world: ::

    # emerge --deselect <package>
    # emerge --depclean -av
