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
                        "alterId": 6
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
    

Thanks for reading :)

References
----------

`OpenWRT x86 Installation
<https://openwrt.org/docs/guide-user/installation/openwrt_x86>`_

`OpenWRT init scripts
<https://openwrt.org/docs/techref/initscripts>`_
