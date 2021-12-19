关于 v2ray sniffing
===================

:Published: : 2021/04/04

.. meta::
    :description: 关于 v2ray 的 sniffing 参数使用，个人的一些理解。

v2ray 的 inbound 配置中有个 sniffing 参数，官方文档对它概念描述很模糊，
目前只知道开启后可以通过 outbound 来解析域名，但更具体的使用就不清楚了。

所以这里根据我实际使用之后的思考，得到的一些猜想和结论，记录下来，不求保证完全正确。

当 inbound 是 socks5, http 之流的代理时，原始数据包会经过 TCP/IP 的层层协议发给代理服务 —— v2ray，
v2ray 解开数据包后会得到目标的域名，因为开启了 sniffing，所以 v2ray 会通过内部的路由规则将域名解析任务交给某个 outbound 处理。

当 inbound 被设置成透明代理时（redirect 或者 tproxy），一般都是配合 iptables 规则使用。
原始数据包在到达 v2ray 时会先经过 iptables，但在这之前就已经把目标域名给解析成 IP 了，否则怎么去匹配 iptables 的规则呢？
大多数的程序都是调用 glibc 中的 getaddrinfo, gethostbyname 函数来交给系统解析 IP 的。
所以这个时候到达 v2ray 的都是 IP，sniffing 是否启用都不影响了，v2ray 不会帮我们解析域名。
因此，我们需要自己部署 dns resolver 来处理 dns 污染的问题。

猜想关于程序何时会解析域名
--------------------------

当一个程序没有使用 socks5, http 等代理时，其不会调用 getaddrinfo, gethostbyname 来解析域名，而是把数据包一股脑发给代理。
只能说大部分程序是这样的，例如 Firefox 的代理配置中有个选项可以选择 socks5 代理之后是否同时代理 DNS 请求（Proxy DNS when using SOCKS V5)，
所以在 Firefox 中，即使使用了 socks5 代理，也可以不通过代理来解析域名。

但一个程序使用的是透明代理（也相当于没有使用代理），在其内部会调用 getaddrinfo, gethostbyname 来解析域名。

Updated 2021/06/10
------------------

在 stackexchange 上看到一个这个 `回答 <https://askubuntu.com/a/447881>`_ ，
http proxy 只能通过 remote 来解析 IP，而 socks5 可以设置通过 local 还是 remote 来解析 IP。

我自己用 tinyproxy —— 一个 http proxy —— 验证了下，果然 DNS 的解析是在 remote 处理的。

另外还看到了一个 `回复 <https://stackoverflow.com/a/34103057>`_ ，
证实了使用 socks5 proxy 可以设置 DNS 在哪里解析。

Thanks for reading :)

References
----------

- `linux dns lookup <https://zwischenzugs.com/2018/06/08/anatomy-of-a-linux-dns-lookup-part-i/>`_
