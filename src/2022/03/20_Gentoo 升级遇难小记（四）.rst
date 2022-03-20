Gentoo 升级遇难小记（四）
=========================

:Published: 2022/03/20

.. meta::
    :description: Gentoo 更新系统的时候遇到了 USE flag 冲突导致软件被跳过更新的问题。

最近又来升级笔记本上的 Gentoo，但是遇到软件冲突导致某软件被跳过安装的问题： ::

    $ sudo emerge --ask --verbose --update --newuse --deep @world

    These are the packages that would be merged, in order:

    Calculating dependencies... done!

    Total: 0 packages, Size of downloads: 0 KiB

    WARNING: One or more updates/rebuilds have been skipped due to a dependency conflict:

    media-gfx/qrencode:0

      (media-gfx/qrencode-4.1.1:0/4::gentoo, ebuild scheduled for merge) USE="-png -test" conflicts with
        media-gfx/qrencode[png(+)] required by (app-admin/pass-1.7.4-r2:0/0::gentoo, installed) USE="git -X -dmenu -emacs -importers -wayland"



    Nothing to merge; quitting.

可以看到 media-gfx/qrencode-4.1.1 与 app-admin/pass-1.7.4-r2 产生了冲突导致前者无法更新。
但首先看下 qrencode 在当前系统的版本： ::

    $ equery l media-gfx/qrencode
     * Searching for qrencode in media-gfx ...
    [IP-] [  ] media-gfx/qrencode-4.1.1:0/4

可以看到 media-gfx/qrencode 目前已经是 4.1.1 版本，那么此次更新只可能是 USE flag 的变动导致的。
通过二者的 ebuild 源码文件一探究竟。

首先是 */var/db/repos/gentoo/media-gfx/qrencode/qrencode-4.1.1.ebuild* ： ::

    IUSE="png test"

然后是 */var/db/repos/gentoo/app-admin/pass/pass-1.7.4-r2.ebuild* ： ::

    RDEPEND="
            media-gfx/qrencode[png(+)]
            ... (omit remaining content here)
    "

上面的 ``media-gfx/qrencode[png(+)]`` 是什么意思呢？ [#]_
其表示 pass 在运行时依赖 qrencode，且需要后者同时启用 png USE flag。
如果 qrencode 不支持 png USE flag 呢，则假装它支持，且启用了该 USE flag。

而事实上在 qrencode 的 ebuild 源码文件中发现其已经支持了 png USE flag，
但该 flag 默认是非启用状态，同时我们并没有在任何地方声明要启用它，因此导致了冲突。

知晓原因后，就知道怎么解决了： ::

    $ vim /etc/portage/package.use/qrencode.use
        media-gfx/qrencode png

之后查看了这两个 ebuild 文件在官方 github 仓库中的历史修改记录，
发现二者都是在前段时间 2 月 14 号的日子里 [#]_ [#]_，加上的 png USE flag 相关的代码。
估计之后在 pass 的 ebuild 文件中，维护者会将上面的依赖语句更新成 ``media-gfx/qrencode[png]`` ，
因为 qrencode 已经支持 png USE flag 了，不用再假装它支持了。

Thanks for reading :)

References
----------

.. [#] `Atom Use defaults <https://forums.gentoo.org/viewtopic-t-1101562-start-0.html>`
.. [#] `media-gfx/qrencode: Add "png" flag <https://github.com/gentoo/gentoo/commit/7a34377e3277a6a0e2eedd40e90452a44c55f1e6>`_
.. [#] `app-admin/pass: Prepare for new qrencode[png] flag <https://github.com/gentoo/gentoo/commit/ccfd53afd435e73c4d4a754a2e006b7860d93246>`_
