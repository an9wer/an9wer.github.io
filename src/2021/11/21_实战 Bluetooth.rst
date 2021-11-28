实战 Bluetooth
==============

:Published: : 2021/11/21

.. meta::
    :description: 在 Linux (Gentoo) 中安装 bluez 软件，使用蓝牙（bluetooth）功能。

我有一个罗技 K480 蓝牙键盘，这个键盘左侧有个小旋钮，分三个档位，一共可以连接三台设备。
出于某些原因，需要将它连上我的笔记本电脑，作为外接键盘使用。

在 Linux 上使用蓝牙，需要安装 bluez 软件包。在我目前使用的 Gentoo 系统中的安装方式： ::

    # vim /etc/portage/make.conf
        USE="bluetooth"
    # emerge --ask --changed-use --deep @world

安装完成后，启动 bluetooth daemon： ::

    # rc-service bluetooth start

调用 bluetoothctl 命令连接蓝牙设备： ::

    $ bluetoothctl

    如果笔记本有多个蓝牙网卡，通过 MAC 地址指定要使用的蓝牙网卡
    [bluetoothctl] # select <MAC address>

    打开蓝牙网卡
    [bluetoothctl] # power on

    列出蓝牙网卡已经配对成功的蓝牙设备的 MAC 地址
    [bluetoothctl] # devices

    扫描其他蓝牙设备的 MAC 地址
    [bluetoothctl] # scan on

    打开 agent 用于连接其他蓝牙设备
    [bluetoothctl] # agent on

    配对其他蓝牙设备
    [bluetoothctl] # pair <MAC address>

    信任其他蓝牙设备
    [bluetoothctl] # trust <MAC address>

    连接其他蓝牙设备
    [bluetoothctl] # connect <MAC address>

以上通过命令行的方式连接蓝牙设备难免有些繁琐，为了方便也可以使用图形化工具 ——
`blueman <https://github.com/blueman-project/blueman>`_ 。

Q&A
---

- 为什么罗技 K480 蓝牙键盘只有一张蓝牙网卡（一个 MAC 地址）可以同时连接三台设备？

因为蓝牙可以设定不同的 channel，罗技 K480 蓝牙键盘有三个档位，
相当于有三个不同的 channel 用于连接不同的设备，不同 channel 之间的设备不会相互影响。

- bluetoothctl 中的 trust 命令有什么用？

因为每次连接不信任的设备需要重新确认，trush 之后可以免去下次连接的确认提示
（具体可以参考 `这个答案 <https://www.reddit.com/r/linuxquestions/comments/g0rid3/bluetoothctl_what_are_trusted_devices/>`_ ）。


Thanks for reading :)
