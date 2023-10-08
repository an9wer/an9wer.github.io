Vultr 换主机小记
================

:Published: 2018/12/03

.. meta::
    :tags: VPS

大概一个多月前，我发现 Vultr 上新增了 3.5 美金每月的主机，但是日本和洛杉矶线路
都没货，心里有些可惜，这么便宜的主机肯定是很抢手吧。可是最近，3.5 美金每月的主
机居然又有货了，于是我赶紧准备入手一台。

先说明一下，我目前一直在使用的是一台 5 美金每月的主机，主要是用来搭建
Shadowsocks，偶尔会跑一些小任务，但依然感觉有些浪费。而这新出的 3.5 美金每月的
主机虽然只有 512 M 的内存（前者是 1G 的内存），但足以满足我的需求，所以为了省下
这 1.5 美金每月的开支，我决定重新部署一台 Shadowsocks 服务器。

首先，在 Vultr 网站上新建一台主机，机房选择日本，镜像选择 Debian，点击确认之后
主机就开始创建了，这个过程非常快，大概一分钟左右主机就创建好了，同时也会获得一
个公网 ip。接下来要做的事情就是用 ping 试一下这个 ip 是否被墙（因为之前有过被封
ip 的经历，而且 Vultr 存在很多至今都还被封的 ip。如果拿到了这样的 ip，也很简单
，只需要重建一个主机，就会得到一个新的 ip，如此往复，总会得到一个没有被封的 ip
），当然 ping ip 还同时可以测算网速的快慢。这之后最好再用 ssh 命令登录主机在确
认一下，避免端口被墙的问题（之前也遇到过这种情况，ip 没有被墙，ssh 端口却被墙了
）。这样一台新的主机就算创建完成了。

按照这个步骤，我同时新建了大概有六台主机，其中为了校验是否价格更贵的主机网速会
比较好，我还特意新建了一台 20 美金每月的主机，结果发现速度和 3.5 美金每月的主机
差不多。之后用 ping 简单测了一下网速，陆续关闭了网速相对较慢的主机，最后只剩下
两台主机，连同我之间的那台主机一共三台。之后为了进一步筛选出一台网速较快的主机
，我用家中的树莓派搭建的小服务器针对这三台主机连续 ping 了 24 小时，最后计算网
速的平均值，结果发现是还原来的那台主机网速最快，为 198 ms，而另两台 3.5 美金/
每月的主机中较快的一台是 199ms，想想慢了这 1ms，却可以每月剩下 1.5 美金，还是值
得的。

选择好主机之后，我无意中发现 Vultr 提供了自定义镜像的功能，也就是在除官方提供的
Debian, Ubuntu, CentOS, Fedora 镜像之外可以选择其它的 Linux 发行版，包含了
Alpine， Arch，FreeBSD 等。我毫不犹豫地选择了 Arch，因为 Arch 是滚动更新，之后
就不需要考虑服务器系统版本老化的问题了。

在参考 Vultr 官方提供的安装教程（文末列出），并结合自己之前在笔记本上安装 Arch
的经验，我也是成功地安装好了 Arch 系统。之后考虑到安全问题，在新系统中新建一个
用户，并只允许用户使用 ssh key 登录，同时禁用 root 远程登录。然后使用最近写的一
个快速部署 Shadowsocks 的项目 —— `ssd <https://github.com/an9wer/ssd>`_ ，在服
务器上部署好 Shadowsocks。最后，为服务器开启 BBR，进一步提高网速：::

    # sysctl net.core.default_qdisc=fq
    # sysctl net.ipv4.tcp_congestion_control=bbr
    # echo 'sysctl net.core.default_qdisc=fq' >> /etc/sysctl.d/bbr.sh
    # echo 'sysctl net.ipv4.tcp_congestion_control=bbr' >> /etc/sysctl.d/bbr.sh

至此，有关 Vultr 换主机总算告一段落，接下来的重点就是关注服务器的稳定性，好在
Vultr 提供了可视化的面板，方便我对服务器的流量，CPU，磁盘等进行监控。

相关命令
--------

用 root 身份创建用户，之后可以用 *visudo* 命令为用户添加免密使用 *sudo* 的权限
： ::

    # pacman -S sudo
    # useradd -m -g wheel <username>

*/etc/sshd/config* 的相关配置如下（注意，在这之前最好先将 ssh public key 用
*ssh-copy-id* 命令复制到服务器上）： ::

    PermitRootLogin no
    PasswordAuthentication no

Updated 2018/12/11
------------------

最近想着让服务器每天执行一下系统更新，所以在服务器上安装了 cronie ，然后使用
``sudo crontab -e`` 命令，添加了如下内容： ::

    0 5 * * * /usr/bin/pacman -Syu --noconfirm && /sbin/shutdown -r +5

这条命令会让服务器在每天凌晨五点的时候进行系统更新（服务器是日本的，所以相当于
北京时间凌晨 4 点），然后在更新成功后 5 分钟重启服务器。当然，服务器重启之后还
需要自动启动为 Shadowsocks 的容器，我找了一个比较简单的方案：直接在 ``sudo
docker run`` 命令运行容器时加上 ``--restart unless-stopped`` 选项。

Updated 2019/02/01
------------------

在 github 上新建了一个项目 —— `verice <https://github.com/an9wer/verice>`_ ，写
了一些脚本专门用来管理服务器。

Updated 2019/07/09
------------------

在服务端开启 tcp fast open: ::

    echo "net.ipv4.tcp_fastopen = 3" >> /etc/sysctl.d/tfo.conf

Thanks for reading :)

References
----------

How to deploy Arch on vultr?

-   https://www.vultr.com/docs/installing-arch-linux-on-a-vultr-server

-   https://www.vultr.com/docs/install-arch-linux-with-btrfs-snapshotting

-   https://gist.github.com/juniorctl/bd9c0afcc313620aeae9d18876f41a5c
