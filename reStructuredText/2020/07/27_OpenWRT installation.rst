OpenWRT installation
====================

Install OpenWRT on X86 machine: ::

    # dd if=openwrt.img of=/dev/sdX
    # parted /dev/sdX
        resizepart 2 -1
    # resize2fs /dev/sdX2
    # reboot

Use opkg through a proxy: ::

    # export http_server=http://<address>:<port>

Install Wireguard: ::

    # opkg update
    # opkg install wireguard luci-app-wireguard
    # reboot

    # wg genkey > privatekey
    # wg pubkey < privatekey > publickey





