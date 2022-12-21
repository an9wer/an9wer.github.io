Shadowsocks 连接异常小记
========================

:Published:  2019/02/20

.. meta::
    :description: 防火墙升级导致 shadowsocks 连接中断。

年后来公司上班，发现自己的两台 shadowsocks 代理都连接异常，主要表现是代理连接上之后几秒钟就会断掉，过了大概五分钟之后又恢复正常，再次连接后又出现这种情况。
查看 shadowsocks 项目 issues，发现有人和我遇到了 `一样的情况 <https://github.com/shadowsocks/shadowsocks/issues/1393>`_ ，
其中有人提到在 shadowsocks 外面包一层 kcptun 可以解决问题。

不过当时公司其他同事的 shadowsocks 还能使用，我怀疑只是网络的临时抽风，亦或是我使用的服务商的问题，因此我并没有这么做。
但是接下来的两天问题依然存在， 而我也偶然在 YouTube 上看到了 `某个视频 <https://www.youtube.com/watch?v=uL5HTRHrxzk>`_ ，
突然意识到可能是 GFW 升级导致了 shadowsocks 代理异常。

于是我才决定在服务器上部署 kcptun。
同时为了下次搭建方便，顺便写了个 `Dockerfile <https://github.com/an9wer/bpd>`_  。

Updated 2019/02/28
------------------

使用 traceroute 查了一下，数据包应该是在某个路由处被 GFW 绊了：

.. image:: /statics/images/2019/02/20_traceroute.jpg
    :alt: Traceroute

Updated 2021/04/06
------------------

不知从何时起，流行的方案变成了用 https 伪装，也就是在加密协议的外面再套一层 https，这样使得代理流量更加隐蔽。

Thanks for reading :)
