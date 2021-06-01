.. meta::
    :robots: noindex

Linux Sys
=========


NIC: ::

    $ ls /sys/class/net

Speed of NIC: ::

    $ cat /sys/class/net/<interface>/speed

State (up/down/unknown) of NIC: ::

    $ cat /sys/class/net/<interface>/operstate


References
----------

``man 5 sysfs``
