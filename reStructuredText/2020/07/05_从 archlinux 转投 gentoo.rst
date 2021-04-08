从 archlinux 转投 gentoo
========================

当使用了 gentoo 之后，我似乎体验到了转角遇到爱的感觉————这才是符合我审美的
linux distro 。

现在日常以及工作一直用的是 archlinux，大概有一年多的时间，虽然不是很久，但也算
对 archlinux 有一个比较直观的了解（这期间自己也写过一些 package）。总的来说，
archlinux 正如它官方声称的那样，是一个简单的 linux distro。这里说的简单，我认为
可以分为两点：一是官方有很详细的文档，对于新手来说很友好，容易上手；二是它本身
很精简，安装完 linux 内核以及 base 包之后，即可开始你的 linux 定制之旅，前提是
你不用 Gnome，NetworkManager，firewalld 等这些臃肿或者二次封装的软件的话，那这
对你来说是一个福音（例如这里完全可以用 dwm, netctl, iptables 等轻量的软件来替代
）。另外，archlinux 的包很多很全，且很新（而这一点对我来说也是一个不喜欢它的地
方）。

早在使用 archlinux 之前，我就听说过 gentoo 了，但对它的认识只停留在一个 compile
from source 的 linux distro。尝试使用 gentoo 的原因也很简单，我当时在找一个非
systemd 的 linux distro。直到安装并使用一段时间后，我愈加发现它能满足我的一些洁
癖：

1. 从源码安装软件非常 Geek，另外我非常享受代码在 compile 的过程（只是对我笔记本
   CPU 的负载稍稍有些担心）。从源码安装还有一个好处是在 compile 的时候可以指定
   使用哪些库或者不需要哪些库（通过 package.use），从而使软件在 compile 完之后
   完全符合你的需要。

2. 官方 repo 提供的软件比较新，虽然相比 archlinux 来说就没有那么新了，但都是比
   较稳定的软件版本，这也让 gentoo 比 archlinux 更加稳定和安全。

3. 它和 archlinux 一样是一个 simple linux distro，甚至提供了 systemd 的替代者
   openrc。

Update 2021/04/08
-----------------

补充一点，gentoo 会把所有你安装的软件都记录在 */var/lib/portage/world* 文件中，
它是不包含那些在安装时候因为依赖关系连带被安装的软件的（通常是一些 lib 软件）。
这样你就能明确知道你在当前系统用到了哪些软件，下次如果重装系统的话，直接安装把
world 文件里面的软件重装一遍就能恢复。

Thanks for Reading :)
