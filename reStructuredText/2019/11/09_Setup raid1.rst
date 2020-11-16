Setup raid1
===========

最近打算把一些照片和重要的文档存储到电脑上，于是特意买了两块东芝 3TB 7200RPM 的
机械硬盘，安装到我的捡垃圾回来的台式机上（有时间的话另外写一篇 blog 谈论下我是
如何东拼洗凑捡回这台电脑的），然后就开始安装 raid1。

Create raid 1 device: ::

    # mdadm --create /dev/md1 --homehost=any --level=mirror --raid-devices=2 /dev/sda /dev/sdb

After that, check the process of creation command: ::

    # cat /proc/mdstat

Or use ``--detail`` option to get the state of raid device, the *resyncing*
means the creation is still being in process: ::

    # mdadm --detail /dev/md1
    State: clean, resyncing

Thanks for reading :)

References
----------

`Kernel wiki: raid setup
<https://raid.wiki.kernel.org/index.php/RAID_setup>`_
