Gentoo 升级遇难小记
===================

有台 Gentoo 的服务器从去年 9 月份就没更新过系统。于是乎今天饶有兴致来 Update 一
波。

首先更新一下 repo： ::

    # emerge --sync

之后提示告诉我要升级系统最好先升级 *sys-apps/portage* ： ::

    # emerge -av --oneshot sys-apps/portage

结果出现一堆依赖报错，形如 ``Dependency graph slot conflicts`` ，咋回事？

原由是使用 emerge 更新一个单独的 package 通常会导致依赖冲突，相当于想要更新的
package A 依赖 package C 的 v2 版本，而一个没有更新的 package B 依赖 package C
的 v1 版本。emerge 目前还没有办法自动处理这些依赖冲突，所以推荐使用 ``emerge
--ask --verbose --update --newuse --deep @world``  命令把所有软件都更新了。

但我得先更新 *sys-app/portage* 才行啊！还是得靠自己手动解决。

看了下官方 wiki 里面的方案，需要找到这些所有这些冲突的 package B 软件，然后先用
如下命令解决 package B 依赖 package C 的版本问题，最后才能更新 package A： ::

    # emerge -av --oneshot =<packge C v2> <package B>
    # ...
    # emerge -av --oneshot <package A>

但是没有 emerge 参数的支持，这样手动更新太麻烦了！好在找到另一个解决方案：使用
emerge 的 ``--nodeps`` 参数安装所有依赖的 package C，最后安装 packge A： ::

    # emerge -av --oneshot --nodeps <package C>
    # ...
    # emerge -av --oneshot --nodeps <pacakge A>

解决了 *sys-apps/portage* 的更新问题，就可以更新其它软件了。原以为到这里就结束
了。结果在 build gcc 的时候因为内存不足编译失败了，服务器的 512M RAM + 512M
SWAP 看起来不够啊！咋办？

1. 升级服务器内存，没钱！
2. 在其它机器编译，太难！

突然脑筋一转，可以把 swap 的空间扩大啊！ ::

    # dd if=/dev/zero of=swapfile bs=1M count=2048 status=progress
    # chmod 500 /swapfile
    # mkswap /swapfile
    # swapon /swapfile

这样就通过 swap file 扩展了 2G 的内存空间，gcc 也终于顺利编译。

Thanks for reading :)

References
----------

`Dependency graph slot conflicts
<https://wiki.gentoo.org/wiki/Troubleshooting#Dependency_graph_slot_conflicts>`_

`Why is there a dependency conflict when I attempt to upgrade a single package?
<https://wiki.gentoo.org/wiki/Project:Portage/FAQ#Why_is_there_a_dependency_conflict_when_I_attempt_to_upgrade_a_single_package.3F>`_

`What should I do when emerge reports a lot of dependency conflicts involving
built slot-operator (foo/bar:X/Y=) dependencies?
<https://wiki.gentoo.org/wiki/Project:Portage/FAQ#What_should_I_do_when_emerge_reports_a_lot_of_dependency_conflicts_involving_built_slot-operator_.28foo.2Fbar:X.2FY.3D.29_dependencies.3F>`_
