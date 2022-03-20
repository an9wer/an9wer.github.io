Gentoo 升级遇难小记（二）
=========================

:Published: : 2021/12/18

.. meta::
    :description: Gentoo 更新系统的时候遇到了 ldns 和 ldns-utils 两个软件包冲突问题。

这两天更新笔记本电脑上的 Gentoo 系统，
遇到 ldns 与 ldns-utils 两个软件包冲突，
导致整个系统无法更新： ::

    $ sudo emerge -avp ldns

    These are the packages that would be merged, in order:

    Calculating dependencies... done!
    [ebuild     U  ] net-libs/ldns-1.8.0-r4:0/3::gentoo [1.7.1-r5:0/3::gentoo] USE="dane ecdsa -doc -ed448 -ed25519 -examples% -gost -python -static-libs -vim-syntax" PYTHON_SINGLE_TARGET="python3_9 -python3_8 (-python3_10)" 1,254 KiB
    [blocks B      ] <net-dns/ldns-utils-1.8.0-r2 ("<net-dns/ldns-utils-1.8.0-r2" is soft blocking net-libs/ldns-1.8.0-r4)

    Total: 1 package (1 upgrade), Size of downloads: 1,254 KiB Conflict: 1 block (1 unsatisfied)

     * Error: The above package list contains packages which cannot be
     * installed at the same time on the same system.

      (net-dns/ldns-utils-1.7.1:0/0::gentoo, installed) pulled in by
        net-dns/ldns-utils required by @selected

      (net-libs/ldns-1.8.0-r4:0/3::gentoo, ebuild scheduled for merge) pulled in by
        ldns
        >=net-libs/ldns-1.7.1[dane?,ecdsa?,ed25519?,ed448?,gost?] (>=net-libs/ldns-1.7.1[dane]) required by (net-dns/ldns-utils-1.7.1:0/0::gentoo, installed) USE="dane ssl -ecdsa -ed25519 -ed448 -examples -gost"


    For more information about Blocked Packages, please refer to the following
    section of the Gentoo Linux x86 Handbook (architecture is irrelevant):

    https://wiki.gentoo.org/wiki/Handbook:X86/Working/Portage#Blocked_packages

可以看出，
目前系统已经安装的是 net-dns/ldns-utils-1.7.1 和 net-libs/ldns-1.7.1-r5，
这次是将后者更新到 net-libs/ldns-1.8.0-r4，
但是因为 ``<net-dns/ldns-utils-1.8.0-r2`` 无法满足要求导致不能更新。

为什么 ldns-utils 不能随之更新到 net-dns/ldns-utils-1.8.0-r2 或者更高的版本呢？
还是让我们通过 ebuild 文件源码一探究竟。

先查看 */var/db/repos/gentoo/net-libs/ldns/ldns-1.8.0-r4.ebuild* 文件，
可以发现 ldns-1.8.0-r4 无法兼容低于 ldns-utils-1.8.0-r2 的版本： ::

    RDEPEND="${COMMON_DEPEND}
            !<net-dns/ldns-utils-1.8.0-r2
    "

再查看 */var/db/repos/gentoo/net-dns/ldns-utils/ldns-utils-1.8.0-r2.ebuild* 文件，
KEYWORDS 中 amd64 有个 ``~`` 前缀，表示其为 unstable 版本，无法直接安装： ::

    KEYWORDS="~alpha ~amd64 ~arm ~arm64 ~hppa ~ia64 ~m68k ~mips ~ppc ~ppc64 ~s390 ~sparc ~x86"

这样就说的通之前安装报错的问题了。既然明白了原因，那么也就有解决方案了：

1. 编辑 */etc/portage/package.mask* 文件，将 ``>net-libs/ldns-1.7.1-r5`` 添加到其中，
   这样 ldns 最多只能更新到 net-libs/ldns-1.7.1-r5，即保留了当前 ldns 的版本。
2. 或者，编辑 */etc/portage/package.accpet_keywords* 文件，将 ``net-dns/ldns-utils ~amd64`` 添加到其中，
   这样就能允许系统安装 net-dns/ldns-utils-1.8.0-r2 版本的 ldns-utils 了。
    
不过上面两种方法都有些问题：
方法一，之后都无法将 ldns 更新到最新的版本；
方法二，安装 unstable 版本的 ldns-utils 似乎没那么可靠。

看起来是时候到官方 `Bugzilla <https://bugs.gentoo.org/>`_ 提个 issue 了。

不过提交前试着搜索 ldns 相关的 issue，
结果还真有和我遭遇相同，且是近期发布的 `issue <https: //bugs.gentoo.org/828109>`_ ,
这里面提到：

    Given that ldns and ldns-utils are built from the same source code, I would
    suggest consolidating them into a single package. This will avoid any
    possible issues with mismatched library versions.

原来是维护者打算把 ldns-utils 合并到 ldns 中成为同一个软件包，继而取消 ldns-utils 软件包。
之所以会出现以上我遇到的问题，是维护者故意为止，让用户自己将 ldns-utils 从 @world 中 deselect： ::

    $ sudo emerge --deselect net-dns/ldns-utils

请问维护者这是哪门子逻辑？

Thanks for reading :)
