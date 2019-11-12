Util-linux mount
================

List all mounted filesystems: ::

    # mount

List all mounted filesystems with labels: ::

    # mount -l

Mount all filesystems mentioned in */etc/fstab*, except for those whose line
contains the noauto keyword: ::

    # mount -a


Filesystem-independent mount options
------------------------------------

default
    Use the default options: rw, suid, dev, exec, auto, nouser, and async.

    **Note** that the real set of all default mount options depends on kernel
    and filesystem type.

auto
    Can be mounted with the ``-a`` option.

noauto
    Can only be mounted explicitly.

exec
    Permit execution of binaries.

dev
    Interpret character or block special devices on the file system.

nodev
    Do not interpret character or block special devices on the file system.

user
    Allow an ordinary user to mount the file system.

    **Note** that this option implies the options noexec, nosuid, and nodev,
    unless overridden by subsequent options.
    
nouser
    Forbid an ordinary user to mount the filesystem.

async
    All IO to the file system should be done asynchronously.

sync
    All IO to the filesystem should be done synchronously.

    In the case of media with a limited number of write cycles (e.g. some flash
    derives), sync may cause life-cycle shortening.

dirsync
    All directory updates wthin the filesystem should be done synchronously.

    This affects the following systemcalls: ``create``, ``link``, ``unlink``,
    ``symlink``, ``mkdir``, ``rmdir``, ``mknod`` and ``rename``.

suid
    Honor set-user-ID and set-group-ID bits or file capabilities when executing
    programs from this filesystem.

nosuid
    Do not honor set-user-ID and set-group-ID bits or file capabilities when
    executing programs from this filesystem.


Non-superuser mounts
--------------------

When */etc/fstab* contains the ``user`` option on a line, any body can mount
the corresponding filesystem: ::

    # vim /etc/fstab
        /dev/sd<X>  /mnt  ext4  default,user
