关于 Linux Kernel Modules
=========================

:Published: : 2021/03/01

.. meta::
    :description: 折腾 Wireguard 的时候顺带了解一些 Linux Kernel Modules 相关的知识。

这几天在尝试给 Gentoo 安装 Wireguard。
当前我的 Kernel 版本是 5.4.97，参考官方 wiki 的说法，Kernel 5.6 及以上的版本已经集成了 Wireguard kernel module，
而我这个版本的 Kernel 需要在 build 的时候开启一些指定的 Kernel modules。

照着文档小心翼翼地开启了 Kernel 的相关配置，
等到 build 完之后发现 5.4.97 版本的 kernel 本身就有 wireguard 模块，
不是说好的 5.6 及以上版本才有的吗？
所以其实不需要特别的 Kernel 配置就可以使用 Wireguard 啊！

不过还是顺带着了解下 Linux kernel modules 是个啥？

在配置 Kernel 的 *.config* 中发现关于 Kernel modules 的 ``CONFIG_XXX`` 值大致可以分为三种 (y/n/m)，
y 表示开启该配置选项并在 build 的时候编译到生成的内核文件中，
n 表示关闭该配置选项，
m 表示 开启该被指选项并在 build 的时候编译成一个独立的模块，可在之后自由地被内核加载或者移除。

使用 ``modprobe`` 命令可以加载或者移除某些 Kernel Modules，
但通常我们都不会手动来操作 Kernel Modules，
了解到似乎是由 ``udev`` 来监听 event 触发 Kernel Modules 的相关操作，像是某些设备的热插拔等。

Thanks for reading :)
