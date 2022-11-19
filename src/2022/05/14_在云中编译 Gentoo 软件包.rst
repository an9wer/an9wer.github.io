在云中编译 Gentoo 软件包
========================

:Published:  2022/05/14

.. meta::
    :description: 为了凸显服务器更多的存在价值，也为了压榨服务器的每一点资源，
        我打算将个人笔记本上系统的日常更新过程挪到服务器上 —— 实现云中编译 Gentoo 软件包。

`前文 </2022/05/01_腾讯云安装%20Gentoo.html>`_ 中，
我在腾讯云上安装了 Gentoo 系统，虽然也给它搭建了一些基础服务，但这对服务器的开销是非常小的。
为了突显服务器更多的存在价值，也为了压榨服务器的每一点资源，我打算将个人笔记本上系统的日常更新过程挪到服务器上 —— 实现云中编译 Gentoo 软件包。

至于如何实现远程编译软件，然后安装到本地呢？
这就得靠 distcc 这个工具了，好在 Gentoo portage 也集成了这个软件。 [#]_

首先需要在本地和远程都安装 distcc 软件： ::

    $ sudo emerge -av distcc

本地和远端之间的通信有两种方式：

1. 通过 tcp socket：好处是 network io 相对比较快，坏处是通信过程全部明文，在公网环境不太安全，不过可以通过配合 wireguard 解决。
2. 通过 ssh：好处是通信过程全部加密，坏处是每次通信都需要建立 ssh 连接，开销比较大，导致 network io 比较慢。

通过 tcp socket
---------------

此方法需要在远端启动 distcc daemon： ::

    $ sudo vim /etc/conf.d/distccd
        DISTCCD_OPTS="${DISTCCD_OPTS} --listen <address> --port <port>"
    $ sudo rc-service distccd start

在本地配置 distcc slaver 地址： ::

    $ sudo vim /etc/distcc/hosts
        <address>:<port>

同时配置 Gentoo portage 启用 distcc： ::

    $ sudo vim /etc/portage/make.conf
        MAKEOPTS="-j1 -l0"
        FEATURES="distcc -network-sandbox"

通过 ssh
--------

这种方式需要提前配置 ssh 的连接方式，且为了避免繁琐地输入登录密码，所以推荐使用 ssh key 的方式登录远端。
另外，由于 portage 用户的家目录在 */var/lib/portage/home* ，所以 ssh 客户端的配置文件都写入在该目录下。

在本地配置 distcc slaver 地址： ::

    $ sudo vim /etc/distcc/hosts
        <ssh host>

同时配置 Gentoo portage 启用 distcc，并使用 ssh 通信： ::

    $ sudo vim /etc/portage/make.conf
        DISTCC_SSH="ssh"
        MAKEOPTS="-j1 -l0"
        FEATURES="distcc -network-sandbox"

DEBUG
-----

如果在调试的过程中遇到问题，可以通过如下方式在开启 distcc 的 DEBUG 模式： ::

    $ sudo vim /etc/portage/bashrc
        export DISTCC_VERBOSE=1
        export DISTCC_SAVE_TEMPS=1
        export DISTCC_FALLBACK=0

Thanks for reading :)

References
----------

.. [#] `Gentoo distcc <https://wiki.gentoo.org/wiki/Distcc>`_
