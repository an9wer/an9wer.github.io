Setup lvm
=========

:Published: : 2020/11/15

.. meta::
    :description: 使用 LVM 给笔记本的存储盘分区，同时方便满足以后扩容的需求。

我现在正在使用的是一台 HP EliteBook 8470p 笔记本。
它本身是带个光驱盘的，不过我把光驱盘取下来换成了一块 2.5 寸的机械硬盘，
用来挂载到用户目录下的 Pictures, Downloads 等。

由于这块机械硬盘有 1TB 的容量，且我目前的用量需求也不完全明确，
所以决定使用 LVM，这样可以在有需要的时候实现动态扩容。

创建一个新的挂载点
------------------

Initialize a new physical volume: ::

    # pvcreate /dev/sd<X>

Create a new volume group: ::

    # vgcreate <vg name> /dev/sd<X>

Create a new logical volume to use all left space in the volume group created above: ::

    # lvcreate -l +100%FREE -n <lv name> <vg name>

Format the logical volume: ::

    # mkfs.ext4 /dev/<vg name>/<lv name>
    
Update fstab file, add the following line: ::

    /dev/<vg name>/<lv name> <mount point> ext4 defaults,noauto,user 0 0

Mount logical volume: ::

    $ mount <mount point>

Set ownership of usr and group for mount point: ::

    # chown -R <uid>:<gid> <mount point>

创建另一个新的挂载点
--------------------

Initialize a new physical volume: ::

    # pvcreate /dev/sd<XX>

Extend an existed group volume: ::

    # vgextend <vg name> /dev/sd<XX>

Create a new logical volume to use all left space in the volume group: ::

    # lvcreate -l +100%FREE -n <lv name> <vg name>

Format the logical volume: ::

    # mkfs.ext4 /dev/<vg name>/<lv name>

扩展某个挂载点的容量
--------------------

Initialize a new physical volume: ::

    # pvcreate /dev/sd<XXX>

Extend an existed group volume: ::

    # vgextend <vg name> /dev/sd<XXX>

Extend an existed logical volume to use all left space in the volume group: ::

    # lvextend -l +100%FREE /dev/<vg name>/<lv name>

Extend ext4 partition on the logical volume: ::

    # resize2fs /dev/<vg name>/<lv name>

Thanks for reading :)
