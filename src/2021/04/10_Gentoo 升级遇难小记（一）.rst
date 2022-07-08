Gentoo 升级遇难小记
===================

:Published: : 2021/04/10

.. meta::
    :description: Gentoo 更新系统的时候遇到了软件包依赖问题，以及在编译 gcc 的时候内存不足的问题。

有台 Gentoo 的服务器从去年 9 月份就没更新过系统，于是乎今天饶有兴致来 Update 一波。

首先更新一下 repo： ::

    # emerge --sync

之后提示告诉我要升级系统最好先升级 *sys-apps/portage* ： ::

    # emerge --oneshot sys-apps/portage

结果出现一堆依赖报错： ::

    !!! Multiple package instances within a single package slot have been pulled
    !!! into the dependency graph, resulting in a slot conflict:

这是咋回事？

原由是使用 emerge 更新一个单独的 package 通常会导致依赖冲突。
例如，想要安装 package A，其依赖 package C 的 v2 版本，
所以需要将系统中已经安装的 package C 从 v1 版本更新到 v2 版本，
但是另一个已经安装的 package B 却依赖 package C 的 v1 版本，不过同时也兼容 v2 版本。
emerge 目前还没有办法自动处理这样依赖冲突，
所以官方推荐使用 ``emerge --ask --verbose --update --newuse --deep @world``  命令一次性把所有软件都更新了。

    Attempts to upgrade single packages will often trigger dependency conflicts
    because emerge does not have an option to specify that it should
    automatically update reverse dependencies as needed. The recommended
    practice is to update all packages together (after each emerge --sync
    operation), using a command such as emerge --deep --newuse --update @world. 

但我得先更新 *sys-app/portage* 这一个软件包才行啊！看来还是得靠自己手动解决。

根据官方 wiki 提供的 `方案 <https://wiki.gentoo.org/wiki/Troubleshooting#Dependency_graph_slot_conflicts>`_ ，
先使用如下命令使 package B 重新依赖 package C 的 v2 版本，
然后安装 package A： ::

    # emerge -ask --oneshot =<packge C v2> <package B>
    # emerge -ask <package A>

但是这种方法会有个问题，假设在更新 packge C 到 v2 版本的时候也遇到了相似的依赖冲突问题，这样循环下去会相当麻烦！
另外假设 package B 也有更新，而其原来版本的 ebuild 文件因为太老被 drop 了，这样就再也无法解决 packge B 与 packge C v2 的冲突问题了。

有个简单且讨巧的方法是使用 emerge 的 ``--nodeps`` 参数直接安装 package C 的 v2 版本，之后安装 packge A： ::

    # emerge -ask --oneshot --nodeps =<package C v2>
    # emerge -ask <pacakge A>

不过需要注意的是：使用 ``--nodeps`` 不总会成功，可能会遇到安装失败的问题，所以这种方法不是完美的。

使用上面的方法将 *sys-apps/portage* 所依赖的软件包都更新之后，就可以更新 *sys-apps/portage* 了。

接下来再使用 ``emerge --ask --verbose --update --newuse --deep @world`` 命令更新其它软件。
原以为到这里就结束了，结果在 build gcc 的时候因为内存不足编译失败了，服务器的 512M RAM + 512M SWAP 看起来不够啊！咋办？

1. 升级服务器内存，没钱！
2. 在其它机器编译，太难！

突然脑筋一转，可以把 swap 的空间扩大啊！ ::

    # dd if=/dev/zero of=/swapfile bs=1M count=2048 status=progress
    # chmod 600 /swapfile
    # mkswap /swapfile
    # swapon /swapfile

这样就通过 swap file 扩展了 2G 的内存空间，gcc 也终于顺利编译。

Thanks for reading :)

References
----------

- `Gentoo Wiki: Why is there a dependency conflict when I attempt to upgrade a single package? <https://wiki.gentoo.org/wiki/Project:Portage/FAQ#Why_is_there_a_dependency_conflict_when_I_attempt_to_upgrade_a_single_package.3F>`_
- `Gentoo Wiki: What should I do when emerge reports a lot of dependency conflicts involving built slot-operator (foo/bar:X/Y=) dependencies? <https://wiki.gentoo.org/wiki/Project:Portage/FAQ#What_should_I_do_when_emerge_reports_a_lot_of_dependency_conflicts_involving_built_slot-operator_.28foo.2Fbar:X.2FY.3D.29_dependencies.3F>`_
