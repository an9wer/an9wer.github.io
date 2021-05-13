关于 chroot
===========

:Published: : 2021/03/20

.. meta::
    :description: 关于 chroot 的一些应用场景，以及其与 docker 的对比。

最初接触 chroot 可能是在安装 arch 和 gentoo 镜像的时候，通过 chroot 切换到安装
的系统目录下面进行初始化配置。

后来慢慢地也用 chroot 做一些其它的事情，例如：

1. 程序软件包的打包。我自己维护了 Arch/Gentoo/RPM 的一些软件包，所以在需要更新
   软件包的时候会切换到 chroot 里面操作。
2. 程序的安装及试用。有时候不想让系统里面装一些杂七杂八的软件，所以会先在
   chroot 里面安装试用，避免污染了整个系统。

其实 chroot 的很多使用场景都和 docker 重叠了，甚至 docker 在某些方面会更加强大
，但是也算是一种更轻量的方案，各位有兴趣不妨也体验下吧。

Thanks for reading :)
