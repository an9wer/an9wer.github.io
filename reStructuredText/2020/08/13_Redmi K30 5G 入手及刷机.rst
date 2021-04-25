Redmi K30 5G 入手及刷机
=======================

自从 Essential Phone 屏幕摔坏之后，一直将就使用已经退役的 Nubia Z5 mini，忍受着
它放口袋里莫名其妙地重启，每次开机需要二十分钟，打开支付宝付款、扫小蓝车需要等
上好长时间，等诸多问题。虽然大部分时候都是可以接受的，但我还是好几次遇到它无故
重启且开机时间过长导致要做的事情被耽误。其中有两次是在坐地铁的时候，导致我出站
无法扫码；还有一次是出差的过程中，直接导致我不能打的（这次事件还有另外一个教训
是身边需要常备一些现金）。虽然只是偶尔发生，但在关键的时候掉链子还是比较头疼，
且严重浪费了我的时间，毕竟时间也是金钱。

所以换个新手机也是迫在眉睫。本来一直觊觎 One Plus，主要是因为刷 Google 比较方便
，奈何它只做高端机，售价超过我的接受范围（很多高级的功能对我来说其实也是可有可
无)。而即便 One Plus 刚上市（目前只在印度和欧洲上市）的 nord，折算成人民币也要
三千多的售价，所以实在是望而却步。另外，这次换手机还有一个耿耿于怀的点，就是手
机需要支持 5G，虽然目前来看 5G 的概念已经铺垫了有一年多，市场好像还是不温不火，
但秉承着手机要用 4 年的信念，支持 5G 还是很有必要的。

所以最终还是选择了这款 Redmi K30 5G，价格与性能合适，刷机相对方便。当然在很多地
方也做了一些妥协，例如屏幕尺寸过大，镜头突起等。

Unlock bootloader: ::

    Settings -> My device -> All specs -> MIUI version (Keep tapping it to enable developer option)
    Settings -> Additional settings -> Developer option -> Mi Unlock status -> Login Mi account
    Connect the phone to the PC using USB cable
    Poweroff the phone and boot into fastboot mode

    Download latest Mi Unlock Tool from 'https://en.miui.com/unlock/download_en.html'
    login the Mi Unlock Tool on PC with the same Mi account and press unlock botton

Boot into fastboot mode: ::

    Press volume down (-) button and power button

Boot into recovery mode: ::

    Press volume up (+) button and power button

Download xiaomi.eu ROM: xiaomi.eu_multi_HMK305G_V11.0.9.0.QGICNXM_v11-10-Fastboot.zip ::

    unpack zip then:
        # sudo ./linux_fastboot_first_install_with_data_format.sh

小插曲：一开始直接使用 ``./linux_fastboot_first_install_with_data_format.sh``
安装，结果等了有半个小时还没有跑完，感觉像是进程卡死了，于是使用 ``strace -p
<pid>`` 看了一下它的状态，发现是它没有权限读取 ``/sys/bus/usb/`` 文件，所以赶紧
``Ctrl-C`` 结束了它，重新加上 ``sudo`` 再次执行即可。

Update 2020/10/09
-----------------

今天发现这个固件版本无法调用前后的人像镜头，所以相当于少了两个镜头。


Thanks for reading :)


References
----------

https://xiaomi.eu/community/threads/guide-how-to-install-xiaomi-eu-rom-for-redmi-k30-k30-5g.54536/
