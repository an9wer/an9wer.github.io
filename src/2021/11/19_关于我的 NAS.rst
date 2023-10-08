关于我的 NAS
============

:Published: 2021/11/19

.. meta::
    :tags: misc
    :description: 聊聊我的 NAS 的软硬件构成，同时也记录数据盘做 RAID 和加密的过程。

我的 NAS 是东拼西凑而成的：

- U-NAS 两盘位机箱
- 华擎 J3455 主板
- 台达 150W Flex 电源
- 两个东芝 4T 机械硬盘
- 一个东芝 256G SATA 固态硬盘

为了保证供电稳定，同时避免断电的风险，我特意买了一个 300W 的 UPS 不间断供电电源。
不过后来证实与我预期的效果相差甚远，家里停电后只能撑上 15 分钟左右，真是短的可怜。
唯一的好处是停电后会发出蜂鸣声，一旦听到这个声音，我就知道要将 NAS 关机了 —— 15 分钟的电量也只够 NAS 完成一个正常关机程序。

说完了硬件，接下来来聊聊软件。
系统盘上面安装的是 Proxmox（虚拟机）系统，里面虚拟了几个日常使用的系统，
打头的是一个 OpenWRT，用来做其他虚拟机的路由器；
接下来是一个 Windows，偶尔用迅雷或者 QQ 等就全靠它了，因为我身边的物理电脑都不是 Windows；
重头戏是一台 Linux，负责挂载数据盘，平常的备份同步都经过它。

两个机械硬盘组成 RAID 1（参照 `Setup raid 1 </2019/11/09_Setup%20raid1.html>`_ 一文），
然后分区成两个磁盘：一个 150G 大小，是给 PVE 虚拟机做快照备份使用；剩下的都用来做数据存储使用。

数据盘直通（Passthrough）给上面提到的 Linux 使用，
方法是查询数据盘的 id，然后通过下面的命令直通给指定的虚拟机： ::

    # qm set <vmid> -scsi2 /dev/disk/by-id/<diskid>

为什么不直接使用设备名（i.e. /dev/sdc）呢？因为设备名可能会变，而硬盘的 id 是不变的。

接下来进入到 Linux 中，就能发现直通的数据盘。
先使用 dm-crypt 先给整个数据盘加密（参照 `Setup dm-crypt </2020/08/26_Setup%20dm-crypt.html>`_ 一文），
之后再格式化，挂载。

至于我有安装什么特别的软件来提供 NAS 的同步备份服务吗？

答曰：无，唯 rsync 尔！

Thanks for reading :)

References
----------

`Passthrough Physical Disk to Virtual Machine
<https://pve.proxmox.com/wiki/Passthrough_Physical_Disk_to_Virtual_Machine_(VM)>`_
