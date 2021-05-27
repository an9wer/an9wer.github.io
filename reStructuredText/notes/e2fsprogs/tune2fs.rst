.. meta::
    :robots: noindex

E2fsprogs tune2fs
=================

List the contents of the filesystem superblock: ::

    # tune2fs -l <device>

Set percent of reversed filesystem blocks: ::

    # tune2fs -m <percent> <device>

Set number of reversed filesystem blocks: ::

    # tune2fs -r <number> <device>


References
----------

``man tune2fs``
