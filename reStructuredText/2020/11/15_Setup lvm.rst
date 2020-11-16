Setup lvm
=========

我这台惠普的笔记本 EliteBook 8470p（二手淘回来的）有个光驱盘，而我把它提换成了
一块机械硬盘。所以打算把它挂载到系统家目录下的 Pictures, Downloads 等文件夹，用
来存储一些数据文件。

因为我这块机械硬盘有 1TB 的大小，一时间不知道怎么划分比较合适，所以打算用 lvm，
每次只添加 50GB 的空间到 pv 里面，可以在有需要的时候实现动态扩容。

Create a physical volume: ::

    # pvcreate /dev/sd<X>

Create a volume group: ::

    # vgcreate <vg name> /dev/sd<X>

Create a logical volume from the volume group above: ::

    # lvcreate -l 100%FREE -n <lv name> <vg name>

Format the logical voluem: ::

    # mkfs.ext4 /dev/<vg name>/<lv name>
    
Update fstab file, add the following line: ::

    /dev/<vg name>/<lv name> <mount point> ext4 defaults,noauto,user 0 0

Mount logical volume: ::

    $ mount <mount point>

Change usr and group ownersip for mount point: ::

    # chown -R <uid>:<gid> <mount point>

Thanks for reading :)
