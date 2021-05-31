OpenWRT 软路由的安装及配置
==========================

:Published: : 2020/07/27

.. meta::
    :description: 在 PVE 中安装 OpenWRT 虚拟机，作为其他虚拟机的网关使用。在
        NanoPi R2S 上刷入 OpenWRT，安装 wireguard, v2ray 等软件，配置成一台
        软路由。

目前我的 PVE 里面目前有两台虚拟机，一台 Gentoo，一台 Win7，所以打算再安装一台
OpenWRT 虚拟机来作为网关负责其它虚拟机的网络。于是按照如下步骤在虚拟机中安装
OpenWRT，当然这种方法也可以在其它 x86 平台上安装。

首先，OpenWRT 可不像 Ubuntu 一样可以通过系统安装盘（Live CD）来安装系统，而是通
过 dd 命令直接把系统刷到硬盘里面的，所以在 PVE 里面怎么给虚拟机刷入 OpenWRT 系
统呢？还是得先挂载 Ubuntu 系统安装盘（其他 Linux 系统安装盘也都可以），引导进入
Ubuntu 的安装系统，打开终端，下载 OpenWRT 的固件，然后给虚拟机的硬盘（/dev/sdX
）刷入： ::

    # dd if=openwrt.img of=/dev/sdX

固件默认刷入的是 16M /boot 以及 256M / 的分区布局大小，给到 / 分区的大小应该是
不够用的，所以这里扩展下它的尺寸，将磁盘所剩下的空间都划给它： ::

    # parted /dev/sdX
        resizepart 2 -1
    # resize2fs /dev/sdX2
    # reboot

重启后进入 OpenWRT 系统，开始安装需要的软件包。OpenWRT 的 opkg 工具安装软件包的
时候可能下载速度比较慢，可以给它设置代理： ::

    # export http_proxy=http://<address>:<port>
    # opkg update

安装 Wireguard: ::

    # opkg install wireguard luci-app-wireguard
    # reboot

    # wg genkey > privatekey
    # wg pubkey < privatekey > publickey

安装 `openwrt-v2ray <https://github.com/kuoruan/openwrt-v2ray>`_: ::

    Download v2ray-core*.ipk from release page, then:
    # opkg install v2ray-core*.ipk

安装 `luci-app-v2ray <https://github.com/kuoruan/luci-app-v2ray>`_: ::

    # opkg install jshn
    # opkg install ip
    # opkg install ipset
    # opkg install iptables
    # opkg install iptables-mod-tproxy
    # opkg install resolveip
    # opkg remove dnsmasq
    # opkg install dnsmasq-full

    Download luci-app-v2ray*.ipk from release page, then:
    # opkg install luci-app-v2ray_1.5.6_all.ipk
    # opkg install luci-compat
    # reboot

Updated 2021/01/28
------------------

之前买了一台 NanoPi R2S，这两天打算刷入 OpenWRT 作为旁路由使用。

NanoPi R2S 刷入 OpenWRT 的方法可以参照官方文档，这里就不赘述了。

接下来安装和配置 v2ray。这次配置的时候觉得 luci-app-v2ray 安装以及使用太麻烦，
所以直接自己写配置文件： ::

    {
        "log": {
            "logLevel": "error"
        },
        "inbounds": [{
            "protocol": "socks",
            "sniffing": {
                "enabled": true,
                "destOverride": ["http", "tls"]
            },
            ...
        }, {
            "protocol": "http",
            "sniffing": {
                "enabled": true,
                "destOverride": ["http", "tls"]
            },
            ...
        }],
        "outbounds": [{
            "protocol": "vmess",
            ...
        }, {
            "protocol": "freedom",
            "tag": "direct",
            ...
        }],
        "routing": {
            "domainStrategy": "AsIs",
            "rules": [{
                "type": "field",
                "domain": [
                    "geosite:cn"
                ],
                "outboundTag": "direct"
            }]
        }
    }

上面的配置里面，分别开启了 socsk 和 http 两个 inbound，注意这二者都需要开启
sniffing，否则无法通过代理来解析域名；outboud 里面，一个是走代理线路，一个走直
连线路；routing 中设置了国内的域名都走直连线路，其他域名走代理线路。

当然，为了开机自启动，还需要手写 init 脚本，放到 */etc/init.d* 目录下即可： ::

    #!/bin/sh /etc/rc.common

    USE_PROCD=1

    START=99
    STOP=01

    start_service() {
        procd_open_instance
        procd_set_param command /usr/bin/v2ray -config /etc/v2ray/<config.json>
        procd_set_param file /etc/v2ray/<config.json>
        #procd_set_param limits core="unlimited"
        procd_set_param pidfile /var/run/v2ray.pid
        procd_close_instance
    }


Updated 2021/04/04
------------------

socks5 和 http 代理用的时候需要看手动配置，感觉还是太麻烦，所以这次直接上透明代
理。透明代理的好处是，只要在路由器中配置即可，局域网内所有设备直接能无感用上代
理。

v2ray 的配置里添加 redirect outbond： ::

    {
        "log": {
            "logLevel": "error"
        },
        "inbounds": [{
            "protocol": "socks",
            "sniffing": {
                "enabled": true,
                "destOverride": ["http", "tls"]
            },
            ...
        }, {
            "protocol": "http",
            "sniffing": {
                "enabled": true,
                "destOverride": ["http", "tls"]
            },
            ...
         }, {
            "protocol": "dokodemo-door",
            "settings": {
                "network": "tcp",
                "followRedirect": true
            },
            "streamSettings": {
                "sockopt": {
                    "tproxy": "redirect"
                }
            },
            ...
        }],
        "outbounds": [{
            "protocol": "vmess",
            "streamSettings": {
                "sockopt": {
                     "mark": 255
                }
            },
            ...
        }, {
            "protocol": "freedom",
            "tag": "direct",
            "streamSettings": {
                "sockopt": {
                     "mark": 254
                }
            },
            ...
        }],
        "routing": {
            "domainStrategy": "IPIfNonMatch",
            "rules": [{
                "type": "field",
                "domain": [
                    "geosite:cn"
                ],
                "ip": [
                    "geoip:cn"
                ],
                "outboundTag": "direct"
            }]
        }
    }

这里的配置和之前的区别在于添加了 redirect 类型的 dokodemo-door inbound，其无需
开启 sniffing（看下文的解释）。

然后在 OpenWRT 的 luci 管理页面中为 firewall 添加 custom rules，将流量转发到上
面定义的 redirect inbound 中： ::

    iptables -t nat -N V2RAY
    iptables -t nat -A PREROUTING -j V2RAY
    iptables -t nat -A OUTPUT -j V2RAY

    # Ignore v2ray direct outbound traffic
    iptables -t nat -A V2RAY -p tcp -j RETURN -m mark --mark 0xfe
    # Ignore v2ray proxy outbond traffic
    iptables -t nat -A V2RAY -p tcp -j RETURN -m mark --mark 0xff

    # Ignore LANs and any other addresses you'd like to bypass the proxy
    # See Wikipedia and RFC5735 for full list of reserved networks.
    iptables -t nat -A V2RAY -d 224.0.0.0/4 -j RETURN
    iptables -t nat -A V2RAY -d 240.0.0.0/4 -j RETURN
    iptables -t nat -A V2RAY -d 0.0.0.0/8 -j RETURN
    iptables -t nat -A V2RAY -d 127.0.0.0/8 -j RETURN
    iptables -t nat -A V2RAY -d 10.0.0.0/8 -j RETURN
    iptables -t nat -A V2RAY -d 172.16.0.0/12 -j RETURN
    iptables -t nat -A V2RAY -d 192.168.0.0/16 -j RETURN
    iptables -t nat -A V2RAY -d 169.254.0.0/16 -j RETURN

    # Redirect all left tcp requests to v2ray
    iptables -t nat -A V2RAY -p tcp -j REDIRECT --to-ports <v2ray redirect port>

到了这一步，还需要解决 dns 污染的问题，虽然 v2ray 中开启了 sniffing，但还是得在
v2ray 之前，也就是系统这一层，单独找个服务来处理 dns，否则 ip 包经过上面的
iptables rules 根本就无法来到 v2ray（例如我在实际当中发现本站 an9wer.github.io
被污染成 127.0.0.1）。

这里我选择的是 dnscrypt-proxy。不过首先需要暂停 dnsmasq 服务，因为二者的端口有
冲突： ::

    # opkg install dnscrypt-proxy2
    # vim /etc/dnscrypt-proxy/dnscrypt-proxy.toml
        listen_addresses = ['<LAN-IP>:53', '127.0.0.1:53']
    # /etc/init.d/dnsmasq stop
    # /etc/init.d/dnsmasq disable
    # /etc/init.d/dnscrypt-proxy start
    # /etc/init.d/dnscrypt-proxy enable

.. role:: strike
    :class: strike

:strike:`这里不需要配置 dnscrypt proxy 的 forward 规则来实现分流，因为分流是在
v2ray 中处理的，dnscrypt proxy 的作用只是为了让被污染成 127.0.0.1 之类的这些 ip
包能正确的达到 v2ray。`

这里还是需要配置 dnscrypt proxy 的 forward 规则对国内国外域名分流解析，因为 dns
解析完成之后给到 v2ray 的都是 ip ，所以 geosite 的规则不会生效，之后 geoip 的规
则才会起作用。但 dnscrypt proxy 中的 resolvers 都是国外的，对于国内的域名例如百
度淘宝之流的也都解析到了国外的 ip，因此这里用 `dnsmasq-china-list
<https://github.com/felixonmars/dnsmasq-china-list>`_ 来实现 forward 规则，具体
build 过程也就不多赘述了。

本以为这样就完成了，但是重启测试发现 dhcp 服务不起作用了，原来是 dhcp 服务是通
过 dnsmasq 来提供的，而我却把它整个关闭了。因此，需要打开 dnsmasq 的 dhcp 功能
，只禁用它的 dns server 功能： ::

    # uci set dhcp.@dnsmasq[0].port="0"
    # uci commit
    # /etc/init.d/dnsmasq start
    # /etc/init.d/dnsmasq enable

这样整个透明代理就搞定了。NanoPi R2S 也从旁路由升级成为网关路由，区别在于
NanoPi R2S 之前是拉了一根网线连接到路由器 lan 口上的，而现在是路由器拉一根网线
连接到 NanoPi R2S 的 lan 口。一下次老子变成儿子，儿子变成老子，呵呵。

Updated 2021/04/05
------------------

v2ray 内建的 geoip 不够看啊，还是得自己来，把 cn 列表导入 ipset 就行： ::

    # opkg install ipset
    # vim /etc/init.d/ipset
        #!/bin/sh /etc/rc.common

        USE_PROCD=0

        START=18
        STOP=99

        start_service() {
            ipset destroy cn
            ipset restore -file /etc/ipset/cn
        }

        stop_service() {
            ipset destroy cn
        }
    # /etc/init.d/ipset start
    # /etc/init.d/ipset enable

不要忘了在 firewall 中添加绕过 cn 的规则： ::

    iptables -t nat -A V2RAY -m set --match-set cn dst -j RETURN
    
Updated 2021/05/29
------------------

今天 OpenWRT 路由器重启遇到 v2ray 也连接不上 server 的情况。之后发现
dnscrypt-proxy 连接上游一直 timeout，不过想想这也正常，因为 v2ray 连不上导致
dnscrypt-proxy 也连不上。

哪里出问题了呢？突然想到 v2ray 的 server 地址是用域名表示的，而 dnscrypt-proxy
无法工作，所以域名也解析不了了。再一看 */etc/resolv.conf* 果然只设置了一个
nameserver 还就是 dnscrypt-proxy 的监听地址。所以这就是个死循环啊！

解决方法是在 */etc/resolv.conf* 中再添加个 nameserver。

也不知道 OpenWRT 中怎么永久性地修改 */etc/resolv.conf* 中的内容，只发现
*/etc/resolv.conf* 是个软链接，指向 */tmp/resolv.conf* ，那是那个程序创建的
*/tmp/resolv.conf* 呢？索性用 grep 在 */etc/init.d* 目录中搜索了一遍，发现是
*/etc/init.d/dnsmasq* 干的坏事。

于是乎细看了下 */etc/init.d/dnsmasq* 的代码文件，才发现有个 localuse 参数看起来
比较可疑。通过 uci 命令将其值修改成 0： ::

    # uci set dhcp.@dnsmasq[0].localuse='0'
    # uci commit

之后重启路由器，此时发现原先的 */etc/resolv.conf* 还是指向 */tmp/resolv.conf*
，而 */tmp/resolv.conf* 这次又指向了 */tmp/resolv.conf.auto* ，该文件中分别包含
了 wan 和 lan interfaces 设置的 nameserver，与 luci 页面中的配置一致，也就是可
以通过 luci 来修改其值。

至此案件告破。

Updated 2021/05/30
------------------

今天又发现连接 NanoPi R2S 的路由器的 dns 地址不是 OpenWRT 的 ip，原来是 OpenWRT
的 DHCP 没有分配 dns nameserver。

OpenWRT 的 dhcp 是通过 dnsmasq 提供的服务，所以： ::

    # vim /etc/config/dhcp
        config dhcp 'lan'
            list 'dhcp_option' '6,<openwrt ip>,114.114.114.114'

Thanks for reading :)

References
----------

`OpenWRT x86 Installation
<https://openwrt.org/docs/guide-user/installation/openwrt_x86>`_

`OpenWRT init scripts
<https://openwrt.org/docs/techref/initscripts>`_
