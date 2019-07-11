Desktop environment
===================

GTK based:

`Wikipedia: GNOME <https://en.wikipedia.org/wiki/GNOME>`_

`Wikipedia: LXDE <https://en.wikipedia.org/wiki/LXDE>`_ 

`Wikipedia: XFCE <https://en.wikipedia.org/wiki/Xfce>`_

QT based:

`Wikipedia: LXQT <https://en.wikipedia.org/wiki/LXQt>`_

`Wikipedia: KDE <https://en.wikipedia.org/wiki/KDE>`_


Install xfce on CeontOS 7:

::

    # yum install epel-release
    # yum groupinstall "X Window system"
    # yum group install xfce


Switch to graphical target imediately in systemd:

::

    # systemctl isolate graphical.target


Enable graphical target on boot:

::

    # systemctl set-default graphical.target

