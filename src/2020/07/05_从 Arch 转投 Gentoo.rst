从 Arch 转投 Gentoo
===================

:Published: 2020/07/05

.. meta::
    :description: 在使用一年多的 Arch 之后，转到 Gentoo 门下。它是如何吸引我的？和 Arch 相比又有什么异同？

在尝试使用了 Gentoo 之后，我似乎体验到了转角遇到爱的感觉 —— 这才是符合我审美的 Linux Distro 。

在此之前一年多的时间里，我的日常及工作均在 Arch 平台上。
在那期间，算是对 Arch 有一个比较深入的了解，同时也写过一些 AUR Package。
总的来说，Arch 正如官方声称的那样，是一个简单的 Linux Distro。
所谓简单，我以为有两点：
一是官方有详细的文档，对于新手来说非常友好，容易上手；
二是系统本身的精简，安装完 Linux 内核以及 base 包之后，即可开启的 Linux 之旅
（Gnome，NetworkManager，firewalld 之流的臃肿软件，统统可以不要。dwm, netctl, iptables 这些软件简单又实用，何不美哉？）。
另外，Arch 的软件包既多又新，让用户更快体验到软件的新功能，足以让其它 Linux Distro 用户垂涎三尺。

早些年就听说过 Gentoo ，当初刚接触 Linux 以为遥不可及，没想到机缘巧合下就这么相遇了 —— 为了找一个不带 systemd 的 Linux Distro。

在使用 Gentoo 一段时间后，我愈加坚定 Gentoo 就是我想要的 Linux Distro，因为它能够满足我的一些癖好：

1. 它默认的 init system 是 openrc 而不是 systemd。
   当然在 Gentoo 中也可以使用 systemd，这一点 Gentoo 相对于 Arch 来说是更加灵活的。

2. 它是滚动更新系统，能随时保持系统在最新版本。
   相对于 Arch 的滚动更新，Gentoo 官方维护的软件版本通常不会是最最新的，而是偏向软件的稳定性和安全性进而选择合适的版本。

3. 它的软件是从源码编译安装。
   从源码安装的好处是在编译前可以指定需要哪些库不需要哪些库，从而使软件在安装完之后的功能完全符合你的需要，不多也不少。
   另外，看到源码编译时输出的一行行日志，虽然不明所以，但是让人感到非常 geek。

4. 它会在软件更新后保留一份用户之前修改过的配置文件以及一份新版本的配置文件。
   通过 etc-update 命令让用户自己决定如何处理新版本的配置文件。所谓“进可攻退可守也”。

Updated 2021/04/08
------------------

补充一点，Gentoo 会把所有安装过的软件都记录在 */var/lib/portage/world* 文件中，
其中不包含在安装之时因依赖关系连同被安装的软件，例如某些 lib 软件。
这就能一目了然地知道在当前系统用到了哪些软件。
如果下次重装系统的话，只要将 world 文件里面的软件重装一遍就能恢复。

Updated 2021/11/28
------------------

再补充一点，Gentoo 的软件包如果有 9999 版本（例如： ``app-misc/ranger-9999`` ），其表明该软件的最最新的版本，是从软件的源码仓库中把最新代码拉下来编译安装的。
如果要想安装它，以 ``app-misc/ranger-9999`` 为例：

首先 unmask ``app-misc/ranger-9999`` ： ::

    # vim /etc/portage/package.accept_keywords
        =app-misc/ranger-9999 **

（可选）为了让 git pull 从仓库拉镜像的时候减少下载数据量，相当于为其加上 ``--depth=1`` 参数，需要设置如下环境变量： ::

    # vim /etc/portage/make.conf
        EGIT_CLONE_TYPE="shallow"

最后在安装时指定 9999 版本： ::

    # emerge -av =app-misc/ranger-9999

Updated 2021/11/30
------------------

再补充一点，有些比较基础的 USE flags 可以在 */etc/portage/make.conf* 中设置成全局的，例如 alsa, opengl 等。
因为我安装了 qutebrowser 之后，使用它看视频发现没有声音，后来才知道是 qtwebengine 在安装的时候没有开启 alsa 这个 flag。
另外值得一提的是：使用 euse 命令可以方便地添加，删除，或者修改全局的 USE flags。

Updated 2021/12/01
------------------

再补充一点，软件通常会有漏洞，Gentoo 官方会针对披露的漏洞对软件进行修复维护，并且展示到官方的 `安全公告平台 <https://security.gentoo.org/glsa/>`_ 。
使用 glsa-check 命令可以方便地查看当前使用的 Gentoo 版本是否存在漏洞，如果有漏洞就需要赶紧升级喽！

Updated 2021/12/19
------------------

Gentoo 之所以在软件更新后，不会随之更新 */etc* 目录下的配置文件内容，
是因为设置了 CONFIG_PROTECT 变量（可以通过 ``emerge --info | grep CONFIG_PROTECT`` 命令查看），
该变量的值是以空格分隔的目录名，这些目录的文件在软件更新的时候都不会被修改。
但如果想设置一些例外的可被修改的目录，则可通过定义另外的一个变量 CONFIG_PROTECT_MASK 实现。

例如，
我想让 emerge 在安装或者更新软件的时候自动将 unmask 提示直接写入到 */etc/portage/package.use/zz-autounmask* 文件中，
但 CONFIG_PROTECT 的值中包含了 */etc* ，
这下就可将 ``CONFIG_PROTECT_MASK="/etc/portage/package.use"`` 添加到 *make.conf* 文件中，
最后在使用 emerge 命令的时候加上 ``--autounmask-write=y`` 参数。

更多描述可以参见 ``man emerge`` CONFIGURATION FILES 章节。

Thanks for Reading :)
