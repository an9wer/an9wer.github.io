Raspberry Pi installation
=========================

::

    $ unzip -p 2019-07-10-raspbian-buster-lite.zip | sudo dd of=/dev/sd<X>


::

    $ sudo vi /etc/default/keyboard    
        XKBLAYOUT="us"
    $ reboot
    

::

    $ sudo iwlist wlan0 scan
    $ sudo vi /etc/wpa_supplicant/wpa_supplicant.conf
        network={
            ssid="testing"
            psk="testingPassword"
        }
    $ sudo wpa_cli -i wlan0 reconfigure

See https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/

::

    $ sudo vim `/etc/apt/sources.list`
        deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib
        deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib

    $ sudo vim `/etc/apt/sources.list.d/raspi.list`
        deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ buster main ui

