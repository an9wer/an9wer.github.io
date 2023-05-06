调节 HP 笔记本的 Trackpoint 灵敏度
==================================

:Published:  2022/03/11

.. meta::
    :description: 在 Linux 系统中，调节 HP 笔记本的 trackpoint 灵敏度。

要知道在若干年前，HP 的 EliteBook 系列的笔记本也是有 trackpoint 的。
而我手上就有这么一台年数已久 HP 笔记本，型号为 EliteBook 8470p。

Trackpoint 还真是个有用的东西，用它来当鼠标，双手可以不用离开键盘核心区域，因此打字和移动鼠标可以无缝切换。
但直到最近，遇到个苦恼的问题 —— 因为使用频率太高，而它默认的灵敏度设置又比较低，导致用久了之后，手指感到异常酸疼。

那么问题来了，在 Linux 下该如何调节 HP 笔记本的 trackpoint 灵敏度呢？

在 Linux 下，input 设备（鼠标，键盘，触摸板等）的驱动主要有 libinput, evdev 和 synaptics。

使用 ``xinput`` 命令可以得知当前 trackpoint 使用的是 libinput，
而同样使用 ``xinput`` 命令修改 trackpoint 灵敏度却不奏效（或者说在 0 到 1  之间的范围内，不管怎么调整，差别都不大）： ::

    $ xinput set-prop 'PS/2 Generic Mouse' 'Libinput Accel Speed' 1

在网上同样看到有人抱怨 libinput 调节的敏感度不及 evdev。 [#]_
于是尝试将 trackpoint 的驱动从 libinput 换成 evdev ，之后 ``xinput`` 的调节果然开始奏效了： ::

    $ sudo vim /etc/X11/xorg.conf
        Section "InputClass"
          Identifier "trackpoint"
          Driver "evdev"
          MatchDevicePath "/dev/input/event<number>"
          Option "ConstantDeceleration" "<number>"
        Endsection

虽然 libinput 是新一代的 input 驱动，但看起来至少对于 HP 笔记本来说，evdev 会更加合适。

Thanks for reading :)

References
----------

.. [#] `Why I've come to dislike libinput <https://www.askwoody.com/forums/topic/why-ive-come-to-dislike-libinput-one-of-the-linux-input-drivers/>`_
