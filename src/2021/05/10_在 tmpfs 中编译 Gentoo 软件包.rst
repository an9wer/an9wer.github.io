在 tmpfs 中编译 Gentoo 软件包
=============================

:Published: : 2021/05/10

.. meta::
    :description: Gentoo 安装软件包或者升级系统的时候，将 /var/tmp/portage 目录挂载成 tmpfs 文件系统，
        安装过程中的读写操作直接写入到内存中，可以减少硬盘的读写次数，增加硬盘寿命，并且提高安装速度。

因为 Gentoo 是通过源码安装软件包，需要下载、解压并编译源代码，这个过程会生成一堆临时文件，对于 SSD 用户来说着实心疼硬盘的寿命。
不过好在可以通过 tmpfs 来缓解硬盘的压力，所谓 tmpfs 即把内存用来当硬盘使用（而 swap 是把硬盘当内存用，正好相反）。

在 Gentoo 安装软件的时候主要会涉及到三个目录：

*/var/cache/distfiles*
    存放软件源代码，一般都是压缩包文件 (.tar.gz)。
    软件包升级后旧的源代码会被删除，只保留最新的源代码。

*/var/tmp/portage*
    存放了软件包在 emerge build 时候的工作目录，软件包的压缩包解压的位置也位于该处。
    软件安装成功后会自动删除该工作目录，但是如果软件安装过程中遇到了 interrupt 问题，则会保留该工作目录。

*/var/cache/binpkgs*
    binary package (目前还不太清楚作用)

由此可以看出，大量的 IO 操作都在 */var/tmp/portage* 目录。
我们对其使用 tmpfs 可以大大提高 SSD 的寿命，甚至也可以节省软件编译时间（因为直接从内存读写文件）。

接下来就是将 */var/tmp/portage* 挂载成 tmpfs 的具体操作： ::

    # vim /etc/fstab
        tmpfs  /var/tmp/portage  tmpfs  size=12G,uid=portage,gid=portage,mode=775,nosuid,noatime,nodev   0 0
    # mount /var/tmp/portage

这里需要指定 */var/tmp/portage* 的大小，
设置太小的话可能都不够软件包源码的解压大小，一般在 emerge build 前会检查是否有足够的空间满足软件包的解压，不够会有警告提示；
设置太大的话会显得浪费，且剩下用来给 emerge build 运行时的内存就不够了。

    size: The limit of allocated bytes for this tmpfs instance. The default is
    half of your physical RAM without swap. If you oversize your tmpfs
    instances the machine will deadlock since the OOM handler will not be able
    to free that memory.

因此我们需要好好地拿捏一下分配给 */var/tmp/portage* 的内存大小。
之后就可以愉快地使用 emerge 安装软件了。

Thanks for reading :)

References
----------

`Gentoo FAQ: What is in /var/tmp/portage?
<https://wiki.gentoo.org/wiki/FAQ#What_is_in_.2Fvar.2Ftmp.2Fportage.3F_Is_it_safe_to_delete_the_files_and_directories_in_.2Fvar.2Ftmp.2Fportage.3F>`_

`Gentoo: Freeing disk space
<https://wiki.gentoo.org/wiki/Knowledge_Base:Freeing_disk_space>`_

`Gentoo: Portage tmpdir on tmpfs
<https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs>`_
