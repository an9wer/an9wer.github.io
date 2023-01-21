Raspberry Pi 安装
=================

:Published: 2019/08/19

.. meta::
    :description: 树莓派安装及配置。

Flash image: ::

    $ unzip -p <x>-raspbian-buster-lite.zip | sudo dd of=/dev/sd<X> bs=4M conv=fsync status=progress

Set keyboard layout: ::

    $ sudo vi /etc/default/keyboard    
        XKBLAYOUT="us"
    $ reboot
    

Add wifi configuration: ::

    $ sudo iwlist wlan0 scan
    $ sudo vi /etc/wpa_supplicant/wpa_supplicant.conf
        network={
            ssid="testing"
            psk="testingPassword"
        }
    $ sudo wpa_cli -i wlan0 reconfigure

Change repository source (see https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/): ::

    $ sudo vim /etc/apt/sources.list
        deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib
        deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib

    $ sudo vim /etc/apt/sources.list.d/raspi.list
        deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ buster main ui

Config NIC eth0: ::

    $ sudo vim /etc/network/interfaces.d/eth0
        auto eth0
        iface eth0 inet static
            address 192.168.12.1/24


Install and config ISC dhcp server: ::

    $ sudo apt install isc-dhcp-server

    $ sudo vim /etc/default/isc-dhcp-server
        INTERFACESv4="eth0"

    $ sudo vim /etc/dhcp/dhcpd.conf
        subnet 192.168.12.0 netmast 255.255.255.0 {
            range 192.168.12.10 192.168.12.250;
        }
        

Install dnscrypt-proxy: ::

    $ sudo apt install dnscrypt-proxy

Install autossh: ::

    $ sudo atp install sutossh


Edit 2019/12/08
---------------

在淘宝上买了 USB 转 TTL 的线，参考 `教程 <https://www.bashpi.org/?page_id=354>`_ ，以后玩树莓排就不需要额外的显示器了。

Thanks for reading :)

References
----------

`RaspberryPi document: config.txt <https://www.raspberrypi.org/documentation/configuration/config-txt/>`_
