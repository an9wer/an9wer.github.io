关于 Linux Kernel Modules
=========================

:Published: 2021/03/01

.. meta::
    :tags: kernel
    :description: 折腾 Wireguard 的时候顺带了解一些 Linux Kernel Modules 相关的知识。

这几天在尝试在 Gentoo 上安装 Wireguard。
参考官方 wiki 的说法，kernel 5.6 及以上的版本已经集成了 wireguard kernel module，
而我目前的 Kernel 版本是 5.4.97，所以在编译的时候需要开启某些 kernel modules。

照着文档小心翼翼地开启了 kernel 的相关配置，
等到编译完之后发现 5.4.97 版本的 kernel 本身就有 wireguard 模块，
不是说好的 5.6 及以上的版本才有吗？
所以原先就不需要特别的配置就可以使用 wireguard 啊！

不过还是顺带着了解下 linux kernel modules 是个啥？

在配置 kernel 的 *.config* 文件中发现关于 modules 的 ``CONFIG_XXX`` 的值大致可以分为三种 (y/n/m)，
y 表示开启该配置选项并在 build 的时候编译到生成的内核文件中，
n 表示关闭该配置选项，
m 表示 开启该被指选项并在 build 的时候编译成一个独立的模块，可在之后自由地被内核加载或者移除。

而使用 ``modprobe`` 命令可以在系统已经启动的状态下动态地加载或者移除 kernel modules，
但一般我们不会手动来操作 kernel modules，
例如 Linux 上设备驱动相关的 modules 一般都是由系统中的 ``udevd`` 监听到 uevent（像是某些设备的热插拔等）之后自动触发 kernel modules 的相关操作。

Thanks for reading :)
