Shadowsocks 连接异常小记
========================

年后来公司，发现我自己的两台 shadowsocks 代理连接异常，主要表现是代理连接上之后
几秒钟就会断掉，过了大概五分钟之后又恢复正常，再次连接后又出现这种情况。后来查
看了 shadowsocks 项目主页，发现有人和我遇到了一样的情况，具体请看 `这个issue
<https://github.com/shadowsocks/shadowsocks/issues/1393>`_ ，回答中有人给出了一
种解决方案：在 shadowsocks 外面包一层 kcptun。

但当时还是有点不以为意，因为公司同事的代理还能用，我猜测可能是临时的网络抽风，
或者是 Vultr 主机出现了网络问题，等修复好就行了。可是接下去的两天问题依然存在，
而且我在 YouTube 上看到了 `这个视频
<https://www.youtube.com/watch?v=uL5HTRHrxzk>`_ ，我突然意识到可能是 GFW 升级导
致了 shadowsocks 代理异常。

于是我才决定在服务器上部署 kcptun，同时为了下次搭建方便，顺便写了个
`Dockerfile <https://github.com/an9wer/bpd>`_ 。

Update 2019/02/28
-----------------

使用 traceroute 查了一下，消息应该是在 GFW 的某个路由处被绊了：

.. image:: /statics/images/2019/02/20_traceroute.jpg
    :alt: Traceroute

Update 2021/04/06
-----------------

不知从何时起，流行的方案变成了用 https 伪装，也就是在加密协议的外面再套一层
https，这样使得代理流量更加隐蔽。

Thanks for reading :)
