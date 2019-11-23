E2fsprogs mk2fs
===============

Specify the percentage (by default is 5%) of the `reserved blocks`_ reserved for
the super-user: ::

    # mk2fs -m <percent> <device>

.. _reserved blocks:

-   reserved blocks

    Reserved blocks are disk blocks reserved by the kernel to avoid `filesystem
    fragmentation <https://en.wikipedia.org/wiki/File_system_fragmentation>`_
    and for processes owned by privileged users to prevent operating system
    from a crash due to unavailability of storage space for critical processes.

    For example, just imagine the size of root file system is 14 GB and the
    root file system is 100% full, all the non privileged user processes would
    not be able to write data to the root file system whereas processes which
    are owned by privileged user (root by default) would still be able to write
    the data to the file system. With the help of reserved blocks, operating
    system keeps running for hours or sometimes days even though root file
    system is 100% full.
