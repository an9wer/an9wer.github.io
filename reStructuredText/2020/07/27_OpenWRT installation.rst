OpenWRT installation
====================

Install OpenWRT on X86 machine: ::

    # dd if=openwrt.img of=/dev/sdX
    # parted /dev/sdX
        resizepart 2 -1
    # resize2fs /dev/sdX2
    # reboot

Use opkg through a proxy: ::

    # export http_proxy=http://<address>:<port>

Install Wireguard: ::

    # opkg update
    # opkg install wireguard luci-app-wireguard
    # reboot

    # wg genkey > privatekey
    # wg pubkey < privatekey > publickey

Install luci-app-v2ray: ::

    # opkg install jshn
    # opkg install ip
    # opkg install ipset
    # opkg install iptables
    # opkg install iptables-mod-tproxy
    # opkg install resolveip
    # opkg remove dnsmasq
    # opkg install dnsmasq-full

    # opkg install luci-app-v2ray_1.5.6_all.ipk
    # opkg install luci-compat
    # reboot





