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
没想到这次疫情封锁期间却派上了大用场。

之所以购入小米 AC2100，主要是三个因素：

1. 可刷 OpenWRT
2. 外观独特（圆筒身材）
3. 价格便宜（入手￥239）

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
    $ wifi up

设置 WiFi 的 SSID 及密码： ::

    $ uci set wireless.default_radio0.ssid='<ssid>'
    $ uci set wireless.default_radio1.ssid='<ssid>'
    $ uci set wireless.default_radio0.encryption='psk2'
    $ uci set wireless.default_radio1.encryption='psk2'
    $ uci set wireless.default_radio0.key='<password>'
    $ uci set wireless.default_radio1.key='<password>'
    $ uci commit wireless
    $ wifi reload

安装 v2ray
----------

从 `此仓库 <https://github.com/kuoruan/openwrt-v2ray>`_ 下载对应版本即可。

安装及配置 iptables
-------------------

安装 ipset： ::

    $ opkg update
    $ opkg install ipset

另外，如果需要 iptables 支持 tproxy，需要安装： ::

    $ opkg install iptables-mod-tproxy

配置 iptables，使其加载 */etc/firewall.user* 文件中自定义的防火墙规则： ::

    $ uci add firewall include
    $ uci set firewall.@include[-1].path='/etc/firewall.user'
    $ uci commit firewall

    $ vim /etc/firewall.user

安装及配置 DNS
--------------

首先关闭默认由 dnsmasq 提供的 DNS 服务： ::

    $ /etc/init.d/dnsmasq stop
    $ uci set dhcp.@dnsmasq[0].port='0'
    $ uci commit dhcp
    $ /etc/init.d/dnsmasq start

安装 dnscrypt-proxy 并配置其监听 lan 口和 lo 口： ::

    $ opkg update
    $ opkg install dnscrypt-proxy2
    $ /etc/init.d/dnscrypt-proxy stop
    # vim /etc/dnscrypt-proxy2/dnscrypt-proxy.toml
        listen_addresses = ['<LAN-IP>:53', '127.0.0.1:53']
    # /etc/init.d/dnscrypt-proxy start

配置 dnsmasq，使其在提供 DHCP 服务的时候将 dns server 设置成 lan 口地址： ::

    # uci add_list dhcp.lan.dhcp_option='6,<LAN-IP>'
    # uci commit dhcp
    # /etc/init.d/network restart

安装及配置 Wireguard [#]_ [#]_
------------------------------

安装 wireguard-tool ： ::

    $ opkg update
    $ opkg install wireguard-tools

配置 wireguard 网口 ： ::

    $ wg genkey | tee wgslave.key | wg pubkey > wgslave.pub
    $ uci set network.wgslave="interface"
    $ uci set network.wgslave.proto="wireguard"
    $ uci set network.wgslave.private_key="<PRIVATE KEY>"
    $ uci add_list network.wgslave.addresses="<SLAVE ADDRESS>"
    $ uci commit network
    $ /etc/init.d/network restart

配置 wireguard 客户端： ::

    $ uci add network wireguard_wgslave
    $ uci set network.@wireguard_wgslave[-1].public_key="<PUBLIC KEY>"
    $ uci set network.@wireguard_wgslave[-1].endpoint_host="<MASTER HOST>"
    $ uci set network.@wireguard_wgslave[-1].endpoint_port="<MASTER PORT>"
    $ uci set network.@wireguard_wgslave[-1].persistent_keepalive="25"
    $ uci set network.@wireguard_wgslave[-1].route_allowed_ips="1"
    $ uci add_list network.@wireguard_wgslave[-1].allowed_ips="<MASTER ADDRESS>"
    $ uci commit network
    $ /etc/init.d/network restart

（其中关于 route_allowed_ips 的作用可以参考
`源代码 <https://github.com/openwrt/openwrt/blob/c03e458c865c837001bb0626061a0e7bd7d8c445/package/network/utils/wireguard-tools/files/wireguard.sh#L85>`_ ）

查看 wireguard 当前配置： ::

    $ wg showconf wgslave

Thanks for reading :)


References
----------

.. [#] `OpenWRT: MI Router AC2100 <https://openwrt.org/toh/xiaomi/mi_router_ac2100>`_
.. [#] `OpenWRT: WireGuard client <https://openwrt.org/docs/guide-user/services/vpn/wireguard/client>`_
.. [#] `Setting up a wireguard server running on an OpenWRT router <https://casept.github.io/post/wireguard-server-on-openwrt-router/>`_
