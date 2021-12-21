在 tmpfs 中编译 Gentoo 软件包（二）
===================================

:Published: : 2021/12/16

.. meta::
    :description: 将 chroot 的根目录挂载点设置成 tmpfs 文件系统，构建一个独立干净的环境，
        用于打包及测试 Gentoo 软件包。

在 `之前一篇文章 </2021/05/10_在%20tmpfs%20中编译%20Gentoo%20软件包.html>`_ 中，
我将 */var/tmp/portage* 使用 tmpfs 文件系统进行挂载，
用于 ``emerge --ask --newuse --update --deep @world`` 命令更新整个 Gentoo 系统时编译软件包，
以减省硬盘的读写量，同时提高编译速度。
这次，我同样会使用 tmpfs，不同的是将它用来构建 Gentoo 软件包的打包及测试环境。

由于自己维护了一个个人的 Gentoo overlay 仓库，需要不定期地给仓库里的软件包升级，
所以需要这样一个打包及测试的环境 —— 当然不能是我本地的系统，主要有两方面的原因，
其一是安装测试软件包可能会破坏当前的系统；其二是本地系统中已经安装了
很多的基础软件包，在打包软件包的时候可能会遗漏其所依赖的软件包。
所以这个环境必须要独立且干净，
因此我想到了在 `之前另一篇文章 </2021/03/20_关于%20chroot.html>`_ 中提到的 chroot。

那么开头提到的 tmpfs 是用来做甚的呢？ —— 我打算将其作为 chroot 挂载点的文件系统使用。
这样做除了之前提到的优点，另外还有一点是：
一旦 unmount chroot，其中所有的内容都会自动消失，
之后打包及测试其他软件包只要重新构建一个全新的 chroot 环境即可，
本地不会留下一堆不知何年何月做甚用的 chroot1，chroot2，chroot3 ……

在本地创建一个目录给 chroot 使用： ::

    $ sudo mkdir /chroot

将 chroot 挂载点设置成 tmpfs 文件系统： ::

    $ sudo mount -t tmpfs -o size=4G,mode=775,nosuid,noatime,nodev tmpfs /chroot

下载 `Gentoo stage tarball <https://www.gentoo.org/downloads/>`_ ，解压到 chroot 目录： ::

    $ sudo tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner -C /chroot

将本地的仓库配置文件以及 DNS resolver 文件复制到 chroot 中： ::

    $ sudo mkdir -p /chroot/etc/portage/repos.conf
    $ sudo cp /etc/portage/repos.conf/gentoo.conf /chroot/etc/portage/repos.conf/gentoo.conf
    $ sudo cp --dereference /etc/resolv.conf /chroot/etc/

将一些必要的文件系统挂载到 chroot 中： ::

    $ sudo mount -o rbind /dev /chroot/dev
    $ sudo mount -t proc none /chroot/proc
    $ sudo mount -o bind /sys /chroot/sys
    $ sudo mount -o bind /tmp /chroot/tmp

由于本地的 */tmp* 目录是与 chroot 共享的，
所以可以将我个人的 overlay 仓库都同步到 */tmp* 目录下，
这样 chroot 里面也可以读取到 overlay 仓库了： ::

    $ rsync -avc /path/to/my-overlay-repo /tmp/my-overlay-repo

之后进入到 chroot 中： ::

    $ sudo chroot /chroot /bin/bash

在 chroot 里面，同步 Gentoo 官方仓库，以及我个人的 overlay 仓库： ::

    (chroot) # emerge --sync gentoo
    (chroot) # emerge --ask app-eselect/eselect-repository
    (chroot) # eselect repository create an9wer /tmp/my-overlay-repo
    (chroot) # emerge --sync an9wer

接下来就可以打包及测试 overlay 仓库中的软件包了。
另外，如果在这过程中发现 chroot 大小不够用了（之前的命令中设置的是 4G 的大小），
可以使用下面的命令直接给其动态扩容，无需 unmount： ::

    $ sudo mount -o remount,size=8G /chroot 

Thanks for reading :)

References
----------

`Gentoo Wiki: chroot  <https://wiki.gentoo.org/wiki/Chroot>`_
