升级 Gentoo Kernel
==================

:Published: : 2021/04/10

.. meta::
    :description: 半个月前同步了最新的 gentoo repo，更新了系统里面安装的所有软件包，
        但是唯独没有编译更新后的 kernel source，今天来了心思，决定操作一把。

半个月前同步了最新的 gentoo repo，更新了系统里面安装的所有软件包，
但是唯独没有编译更新后的 kernel source，今天来了心思，决定操作一把。

首先本地有多个 kernel 版本，选择最新的那个 kernel 版本： ::

    # eselect kernel list
    # eselect kernel set <number>

接下来配置 Kernel 的 .config 文件。
但因为我是使用 ``genkernel all`` 这个傻瓜命令 build kernel，
所以可以跳过配置 .config 文件这一步，直接执行： ::

    # genkernel all

到这里 Kernel 就 build 完成了，接下来就是更新 grub 的配置，使下次重启系统载入最新的 kernel： ::

    # grub-mkconfig -o /boot/grub/grub.cfg

重启电脑： ::

    # reboot

重启后如果没有问题就可以清理旧版 Kernel 了。
可以手动在 */usr/src/* ， */lib/modules* ， */boot/* 目录中找到旧版 Kernel 相关的文件并删除，
亦可使用 eclean-kernel 工具列出并删除： ::

    # emerge --ask app-admin/eclean-kernel
    # eclean-kernel -A -d -n 1

从系统中移除旧版 Kernel 的软件包 ： ::

    # emerge --deselect sys-kernel/gentoo-sources:<old version>
    # emerge --ask --depclean

Thanks for reading :)

References
----------

- `Gentoo wiki: kernel upgrade <https://wiki.gentoo.org/wiki/Kernel/Upgrade>`_
- `Gentoo wiki: kernel removal <https://wiki.gentoo.org/wiki/Kernel/Removal>`_
