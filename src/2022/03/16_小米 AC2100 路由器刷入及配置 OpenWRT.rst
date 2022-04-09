小米 AC2100 路由器刷入及配置 OpenWRT
====================================

:Published: 2022/03/16

.. meta::
    :description: 由于疫情的原因被封锁在家远程办公，但是在家上网冲浪各种不方便，
        于是掏出小米 AC2100 路由器，刷入 OpenWRT，扶墙上网。

由于疫情的原因被封锁在家远程办公，但是上网冲浪各种不方便，
于是掏出小米 AC2100 路由器，架好扶墙新姿势。

要说这台小米 AC2100 还是我两周前在网上买回来的，本是打算用来做中继路由蹭房东家的 WiFi，
但是之后自己办了长城宽带，而运营商给的路由器又有 WiFi 功能，所以这台小米 AC2100 路由器就被闲置了。
没想到这次疫情期间派上了大用场。

之所以购入小米 AC2100，主要是三个因素：

1. 可刷 OpenWRT
2. 价格便宜（入手￥239）
3. 外观独特

刷入 OpenWRT 的过程完全参照官方提供的文档 [#]_，
需要先给路由器固件降级，利用小米官方固件 2.0.722 版本的漏洞，破解路由器 root 帐号的密码；
ssh 登录路由器后即可刷入 OpenWRT 固件，成功后路由器自动重启，重新登录上去后就会发现系统已经变成了 OpenWRT，
此时路由器的地址也已变成 192.168.1.1。

第一次登录刷机后的路由器发现没有 Web 管理界面 —— 因为官方提供的固件默认没有安装 luci 软件包。
那索性尝试下使用 uci 命令来配置对路由器进行管理。

（可选）修改 lan 口的网段，默认为 192.168.1.0/24： ::

    $ uci set network.lan.ipaddr='<ipaddr>'
    $ uci set network.lan.netmask='<netmask>'
    $ uci commit
    $ /etc/init.d/network reload


开启 WiFi： ::

    $ uci set wireless.radio0.country='CN'
    $ uci set wireless.radio1.country='CN'
    $ uci set wireless.radio0.disabled='0'
    $ uci set wireless.radio1.disabled='0'
    $ uci commit wireless
    $ wifi reload

设置 WiFi 的 SSID 及密码： ::

    $ uci set wireless.default_radio0.ssid='<ssid>'
    $ uci set wireless.default_radio1.ssid='<ssid>'
    $ uci set wireless.default_radio0.key='<password>'
    $ uci set wireless.default_radio1.key='<password>'
    $ uci commit wireless
    $ wifi reload

安装 v2ray
----------

从此 `仓库 <https://github.com/kuoruan/openwrt-v2ray>`_ 下载对应版本即可。

安装及配置 iptables
-------------------

安装 iptables ： ::

    $ opkg update
    $ opkg install iptables

但是发现 iptables 居然不支持 nat table，需要另外再安装： ::

    $ opkg install kmod-ipt-nat

如果另外想在 iptables 中支持 tproxy，则需要安装： ::

    $ opkg install iptables-mod-tproxy

配置 iptables，使其： ::

    $ uci add firewall include
    $ uci set firewall.@include[-1].path='/etc/firewall.user'
    $ uci commit firewall

    $ touch /etc/firewall.user

安装及配置 DNS
--------------

首先关闭默认由 dnsmasq 提供的 DNS 服务： ::

    $ /etc/init.d/dnsmasq stop
    $ uci set dhcp.@dnsmasq[0].port='0'
    $ uci commit dhcp
    $ /etc/init.d/dnsmasq start

安装 dnsmasq 并配置其监听 lan 口和 lo 口： ::

    $ opkg update
    $ opkg install dnscrypt-proxy2
    $ /etc/init.d/dnscrypt-proxy stop
    # vim /etc/dnscrypt-proxy/dnscrypt-proxy.toml
        listen_addresses = ['<LAN-IP>:53', '127.0.0.1:53']
    # /etc/init.d/dnscrypt-proxy start

Thanks for reading :)


References
----------

.. [#] `OpenWRT: MI Router AC2100 <https://openwrt.org/toh/xiaomi/mi_router_ac2100>`_
