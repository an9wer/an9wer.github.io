OpenWRT installation
====================

目前我的 PVE 里面目前有两台虚拟机，一台 Gentoo，一台 Win7，所以打算再安装一台
Openwrt 的虚拟机来负责其它虚拟机的网络进出。于是按照如下步骤在虚拟机中安装
OpenWRT，当然这种方法也可以用在 x86 电脑上安装 OpenWRT。

Flash OpenWRT firmware on X86 machine, and enlarge partition size: ::

    # dd if=openwrt.img of=/dev/sdX
    # parted /dev/sdX
        resizepart 2 -1
    # resize2fs /dev/sdX2
    # reboot

Use opkg through a proxy if download speed is low: ::

    # export http_proxy=http://<address>:<port>

Install Wireguard: ::

    # opkg update
    # opkg install wireguard luci-app-wireguard
    # reboot

    # wg genkey > privatekey
    # wg pubkey < privatekey > publickey

Install `v2ray <https://github.com/kuoruan/openwrt-v2ray>`_: ::

    Download v2ray-core*.ipk from release page, then:
    # opkg install v2ray-core*.ipk

Install `v2ray luci <https://github.com/kuoruan/luci-app-v2ray>`_: ::

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

Update 2021/01/28
-----------------

之前买了一台 NanoPi R2S，用来作为旁路由使用。

这次配置的时候觉得 v2ray luci 使用安装和使用起来太麻烦，所以直接自己写配置文件
： ::

    {
        "log": {
            "logLevel": "error"
        },
        "inbounds": [{
            "port": 1080,
            "listen": "0.0.0.0",
            "protocol": "socks",
            "sniffing": {
                "enabled": true,
                "destOverride": ["http", "tls"]
            },
            "settings": {
                "auth": "noauth",
                "udp": false
            }
        }, {
            "port": 1081,
            "listen": "0.0.0.0",
            "protocol": "http",
            "sniffing": {
                "enabled": true,
                "destOverride": ["http", "tls"]
            },
            "settings": {
                "timeout": 0,
                "allowTransparent": false,
                "userLevel": 0
            }
        }],
        "outbounds": [{
            "protocol": "vmess",
            "settings": {
                "vnext": [{
                    "address": "<ADDRESS>",
                    "port": <PORT>,
                    "users": [{
                        "id": "<ID>",
                        "alterId": <ALTERID>
                    }]
                }]
            }
        }, {
            "protocol": "freedom",
            "settings": {},
            "tag": "direct"
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

当然还需要手写 init 脚本： ::

    #!/bin/sh /etc/rc.common

    USE_PROCD=1

    START=99
    STOP=01

    start_service() {
        procd_open_instance
        procd_set_param command /usr/bin/v2ray -config /etc/v2ray/config.json
        procd_set_param file /etc/v2ray/config.json
        #procd_set_param limits core="unlimited"
        procd_set_param pidfile /var/run/v2ray.pid
        procd_close_instance
    }


Update 2021/04/04
-----------------

socks5 和 http 代理用起来还是太麻烦，所以这次直接上透明代理。

v2ray 的配置里添加 redirect outbond： ::

    {
        "log": {
            "logLevel": "error"
        },
        "inbounds": [{
            "port": 1080,
            "listen": "0.0.0.0",
            "protocol": "socks",
            "sniffing": {
                "enabled": true,
                "destOverride": ["http", "tls"]
            },
            "settings": {
                "auth": "noauth",
                "udp": false
            }
        }, {
            "port": 1081,
            "listen": "0.0.0.0",
            "protocol": "http",
            "sniffing": {
                "enabled": true,
                "destOverride": ["http", "tls"]
            },
            "settings": {
                "timeout": 0,
                "allowTransparent": false,
                "userLevel": 0
            }
         }, {
            "port": 1082,
            "listen": "0.0.0.0",
            "protocol": "dokodemo-door",
            "sniffing": {
                "enabled": true,
                "destOverride": ["http", "tls"]
            },
            "settings": {
                "network": "tcp,udp",
                "followRedirect": true
            },
            "streamSettings": {
                "sockopt": {
                    "tproxy": "redirect"
                }
            }
        }],
        "outbounds": [{
            "protocol": "vmess",
            "settings": {
                "vnext": [{
                    "address": "<IP>",
                    "port": <PORT>,
                    "users": [{
                        "id": "<ID>",
                        "alterId": <ALTERID>
                    }]
                }]
            },
            "streamSettings": {
                "sockopt": {
                     "mark": 255
                }
            }
        }, {
            "protocol": "freedom",
            "settings": {},
            "tag": "direct",
            "streamSettings": {
                "sockopt": {
                     "mark": 254
                }
            }
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

然后在 OpenWRT 的 luci 管理页面中为 firewall 添加 custom rules： ::

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
    iptables -t nat -A V2RAY -p tcp -j REDIRECT --to-ports 1082

到了这一步，还需要解决 dns 污染的问题，虽然 v2ray 中开启了 sniffing，但是还是得
在 v2ray 之前也就是系统这一层单独找个服务来处理 dns，否则 ip 包经过上面的
iptables rules 根本就无法来到 v2ray（例如我在实际当中发现 an9wer.github.io 被污
染成 127.0.0.1）。因此，这里使用的是 dnscrypt-proxy。

安装以及启动 dnscrypt-proxy，这里得提前暂停 dnsmasq 服务，因为二者的端口有冲突
： ::

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

这里还需要配置 dnscrypt proxy 的 forward 规则来实现分流，因为 dns 解析完成之后
给到 v2ray 的都是 ip ，所以 geosite 的规则不会生效，之后 geoip 的规则才会起作用
。但 dnscrypt proxy 中的 resolvers 都是国外的，对于国内的域名例如百度淘宝之流的
也都解析到了国外的 ip，因此这里用 `dnsmasq-china-list
<https://github.com/felixonmars/dnsmasq-china-list>`_ 来实现 forward 规则，具体
build 过程也就不多赘述了。

本以为这样就完成了，但是重启测试发现 dhcp 服务不起作用了，原来是 dhcp 服务是通
过 dnsmasq 来提供的，而我却把它整个关闭了。因此，需要打开 dnsmasq 的 dhcp 功能
，只禁用它的 dns server 功能： ::

    # uci set dhcp.@dnsmasq[0].port="0"
    # uci commit
    # /etc/init.d/dnsmasq start
    # /etc/init.d/dnsmasq enable

这样就搞定了。

Update 2021/04/05
-----------------

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
    

Thanks for reading :)

References
----------

`OpenWRT x86 Installation
<https://openwrt.org/docs/guide-user/installation/openwrt_x86>`_

`OpenWRT init scripts
<https://openwrt.org/docs/techref/initscripts>`_
