Gentoo 升级遇难小记（三）
=========================

:Published: : 2021/12/24

.. meta::
    :description: Gentoo 更新 gcc 软件包的时候磁盘空间不足的问题。

之前有幸赶上最后一班 Bandwagon CN2 GIA $49.9/year 的车 —— 现在已成为绝版小鸡。

但万幸中的不幸是，其只有 512M 的内存以及 10G 的磁盘空间，而我还偏偏安装了 Gentoo ——
因此在每次更新 gcc 软件包的时候都是个头疼的问题。
因为一般在更新软件包的时候我会生成 2G 的 swap 充当临时内存，此时磁盘的空间就捉襟见肘了，常常是不够 gcc 编译使用。

想到可以用 NFS 用来扩展磁盘空间，
不过如果在 non-Gentoo 系统上开启 NFS server，同时挂载给 Gentoo 系统的 */var/tmp/portage/* 路径，
然后使用 ``emerge`` 命令安装软件包，会有权限相关的报错。
原因也显而易见，是因为 non-Gentoo 系统上没有 portage 这个用户，
但发现即使手动创建了 portage 用户，依然无法正常使用 ``emerge`` 。
看起来需要 NFS server 所在的系统也同样是 Gentoo。

所以只能新建一个 Gentoo 系统，然后在其上安装 NFS server。
但是众所周知，搭建一个 Gentoo 系统是非常耗时的。
那怎么能快速创建 Gentoo 系统呢？ —— 答案是 stage4。
通常我们都是基于官方提供的 stage3（tar 包）安装 Gentoo 系统的，stage3 中只包含了一些基础的系统文件（bin, lib 等）
而 stage4 的概念则是将一个完整可用的系统都打成 tar 包，解压即可用。

网上有人提供了一些可用的 stage4，不过也可以通过 `mkstage4 <https://github.com/TheChymera/mkstage4>_` 工具
手动将一个完整的 Gentoo 打包成 stage4 tar 包。
之后便可快速安装 Gentoo 系统（与其说是安装，不如说是还原，呵呵）。

NFS server
----------

::

    $ sudo emerge -av net-fs/nfs-utils
    $ sudo vim /etc/exports
        /var/tmp/portage  <client ip>/32(rw,no_root_squash,sync,no_subtree_check,crossmnt,fsid=0)
    $ sudo vim /etc/conf.d/nfs
        OPTS_RPC_NFSD="2 -V 3 -V 4 -V 4.1"
    $ sudo rc-service nfs start

NFS client
----------

::

    $ sudo vim /etc/fstab
        <server ip>:/var/tmp/portage  /var/tmp/portage  nfs  rw,noauto  0  0
    $ sudo rc-service nfsclient start
    $ sudo mount /var/tmp/portage

Thanks for reading :)
