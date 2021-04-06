关于 v2ray sniffing
===================

v2ray 的 inbound 配置中有个 sniffing 参数，官方文档对它概念描述很模糊，目前只知
道开启后可以通过 outbound 来解析域名，但更具体的使用就不清楚了。

所以这里根据我实际使用之后的思考，得到的一些猜想和结论，记录下来，不求保证完全
正确。

当 inbound 是 socks5, http 之流的代理时，原始数据包会经过 TCP/IP 的层层协议发给
代理服务，也就是 v2ray，假设这里是 127.0.0.1:1080，v2ray 解开数据包后会得到目标
的域名，因为开启了 sniffing，所以 v2ray 会通过内部的路由规则将域名解析任务交给
某个 outbound 处理。

当 inbound 被设置成透明代理时（redirect 或者 tproxy），一般都是配合 iptables 规
则使用。原始数据包在到达 v2ray 时会先经过 iptables，但在这之前就已经把目标域名
给解析成 IP 了，否则怎么去匹配 iptables 的规则呢？大多数的程序都是调用 glibc 中
的 getaddrinfo, gethostbyname 函数来交给系统解析 IP 的。所以这个时候到达 v2ray
的都是 IP，sniffing 是否启用都不影响了，v2ray 不会帮我们解析域名。因此，我们需
要自己部署 dns resolver 来处理 dns 污染的问题。

猜想关于程序何时会解析域名
--------------------------

当一个程序没有使用 socks5, http 等代理时，其不会调用 getaddrinfo, gethostbyname
来解析域名，而是把数据包一股脑发给代理。

但一个程序使用的透明代理（也相当于没有使用代理），在其内部会调用 getaddrinfo,
gethostbyname 来解析域名。

Thanks for reading :)

References
----------

`linux dns lookup
<https://zwischenzugs.com/2018/06/08/anatomy-of-a-linux-dns-lookup-part-i/>`_
