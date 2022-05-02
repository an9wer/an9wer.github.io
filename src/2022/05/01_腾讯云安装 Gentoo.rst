腾讯云安装 Gentoo
=================

:Published: 2022/05/01

.. meta::
    :description: 我在腾讯云有一台轻量云服务器，其运行的一直是 CentOS7，这次突发奇想给它安装 Gentoo 系统。

我在腾讯云有一台轻量云服务器，其运行的一直是 CentOS7，这次突发奇想给它安装 Gentoo 系统。

首先下载 Gentoo 系统的 iso 文件到当前系统的根目录下。
然后修改系统的 */boot/grub2/grub.cfg* 文件，添加如下配置 ::

    menuentry "gentoo" {
      set isofile='/install-amd64-minimal-20220102T170545Z.iso'
      loopback loop $isofile
      linux (loop)/boot/gentoo init=/linuxrc dokeymap docache passwd=<PASSWD> dosshd looptype=squashfs loop=/image.squashfs cdroot isoboot=$isofile
      initrd (loop)/boot/gentoo.igz
    }

值得一提的是 linuxrc 这个命令，它是 gentoo ramfs 中的一个类似 init 命令工具，
但是它提供了更多的参数，例如上面的 ``dokeymap``, ``docache``, ``passwd``, ``dosshd`` 等。

- ``dokeymap``: 在载入安装镜像时，提供选项设置 keymap
- ``docache``: 将安装镜像整个载入内存（但在实际运行时发现没有完全载入内存）
- ``passwd``: 设置安装镜像中 root 的密码
- ``dosshd``: 开启 sshd 服务
- ``isoboot``: 载入安装镜像

重启系统后在 grub 引导界面选择 gentoo 进入，即可正常载入 gentoo 的安装镜像。

需要注意的是，gentoo 的安装镜像没有完全载入内存（还没有搞清楚原因），
因此无法对之前系统所在磁盘进行重新分区以及格式化。
所以只能将之前的系统盘挂载到 */mnt/gentoo* 后将所有文件全部删除，
只留下一个 gentoo iso 安装镜像文件。

接下来就是正常的系统安装流程，就不多赘述了。

Thanks for reading :)
