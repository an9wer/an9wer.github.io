Kernel upgrade in Gentoo
========================

半个月前同步了最新的 gentoo repo，更新了系统里面安装的所有软件包，但是唯独没有
build 更新后的 kernel，今天来了心思，决定操作一把。

首先本地有多个 kernel 版本，选择最新的那个 kernel 版本： ::

    # eselect kernel list
    # eselect kernel set <number>

接下来配置 kernel 的 *.config* 文件。但因为我是使用 ``genkernel all`` 这个傻瓜
命令 build kernel，所以可以跳过着配置 *.config* 文件这一步： ::

    # genkernel all

到这里 kernel 就 build 完成了，接下来就是更新 grub 的配置，使开机进入最新的
kernel： ::

    # grub-mkconfig -o /boot/grub/grub.cfg

重启试下，如果没有问题就可以清理旧版本的 kernel 了： ::

    # emerge --deselect sys-kernel/gentoo-sources:<old version>
    # eclean-kernel -d -n 1

这里我只保留了最新一个版本的 kernel。

这样，终于可以把 kernel upgrade 任务从我的 todo list 里面移除了。

Thanks for reading :)

References
----------

`Gentoo wiki: kernel upgrade
<https://wiki.gentoo.org/wiki/Kernel/Upgrade>`_

`Gentoo wiki: kernel removal
<https://wiki.gentoo.org/wiki/Kernel/Removal>`_
