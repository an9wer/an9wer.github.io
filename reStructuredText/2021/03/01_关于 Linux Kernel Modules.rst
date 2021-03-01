关于 Linux Kernel Modules
=========================

这几天在尝试给 Gentoo 安装 Wireguard。当前我的 Kernel 版本是 5.4.xx，参考官方
wiki 的说法，Kernel 5.6 及以上的版本已经集成了 Wireguard kernel module，而我这
个版本的 Kernel 需要在 build 的时候开启一些指定的 Kernel modules。

因此顺带着了解下 Linux kernel modules 是个啥？

在配置 Kernel 的 *.config* 中发现关于 Kernel modules 的 ``CONFIG_XXX`` 值大致可
以分为三种 (y/n/m)，y 表示开启该配置选项并在 build 的时候编译到生成的内核文件中
，n 表示关闭该配置选项，m 表示 开启该被指选项并在 build 的时候编译成一个独立的
模块，可在之后自由地被内核加载或者移除。

使用 ``modprobe`` 命令可以加载或者移除 Kernel Modules，但通常我们都不会手动来操
作 Kernel Modules，了解到好像是由 ``udev`` 来监听 event 触发 Kernel Modules 的
相关操作，像是某些设备的热插拔等。

Thanks for reading :)
