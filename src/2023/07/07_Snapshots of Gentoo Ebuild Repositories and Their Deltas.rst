Snapshots of Gentoo Ebuild Repositories and Their Deltas
========================================================

:Published: 2023/07/07

.. meta::
    :description: What is the command 'emerge-delta-webrsync'? How to use it to
        download snapshots of Gentoo ebuild repositories and their deltas?

Snapshots of Gentoo ebuild repositories are tarball files, which can be
downloaded from any Gentoo mirrors (specified by ``GENTOO_MIRRORS``) through
the command ``emerge-webrsync`` to update local ebuild repositories. Another
less common but useful command ``emerge-delta-webrsync`` can download not only
snapshots, but also their deltas, the different parts between two snapshots.
This is an example of a snapshot directory tree in Gentoo mirrors: ::

    snapshots/
        deltas/
            snapshot-yyyymmdd-yyyymmdd.patch.bz2
            snapshot-yyyymmdd-yyyymmdd.patch.bz2.md5sum
        gentoo-yyyymmdd.tar.xz
        gentoo-yyyymmdd.tar.xz.md5sum
        portage-yyyymmdd.tar.xz
        portage-yyyymmdd.tar.xz.md5sum
        portage-yyyymmdd.tar.bz2
        portage-yyyymmdd.tar.bz2.md5sum

The reason for using deltas instead of snapshots is to minimize download
bandwith and save disk space. A good practice is enabling
``sync-webrsync-delta`` in the file *repos.conf* to use
``emerge-delta-webrsync`` automatically when calling the command ``emerge
--sync <REPO>``: ::

    $ vim /etc/portage/repos.conf/gentoo.conf
        sync-webrsync-delta = yes

Gentoo releases a new snapshot for every single day, which, however, is named
with two different formats, *portage-yyyymmdd.tar.xz* and
*gentoo-yyyymmdd.tar.xz*. Although running md5sum on them returns different
output, files inside them, except the top-level directory (*portage* and
*gentoo-yyyymmdd*), are totally same. It can be verified through the following
commands: ::

    $ tar -xvf portage-yyyymmdd.tar.xz
    $ tar -xvf gentoo-yyyymmdd.tar.xz

    # returns nothing if no difference between them
    $ rsync -acn portage gentoo-yyyymmdd

Or checking the file *metadata/timestamp.commit* inside the snapshot can get
the exact commit id on which that snapshot is based. The snapshots should be
equivalent to each other if they are based on the same commit id: ::

    $ tar -xvf portage-yyyymmdd.tar.xz --strip-components=1 -C portage
    $ cat portage/metadata/timestamp.commit

    $ tar -xvf gentoo-yyyymmdd.tar.xz --strip-components=1 -C gentoo
    $ cat gentoo/metadata/timestamp.commit

As mentioned, both of the command ``emerge-webrsync`` and
``emerge-delta-webrsync`` use snapshots to update local ebuild repositories. In
particular, the former uses the snapshots with the format
*gentoo-yyyymmdd.tar.xz*, and the latter uses the snapshots with the format
*portage-yyymmdd.tar.bz2*. Deltas, instead, are all named with the format
*snapshot-yyyymmdd-yyyymmdd.patch.bz2*.

Thanks for reading :)
