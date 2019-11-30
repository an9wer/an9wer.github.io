Systemd timedatectl
===================

To check the current zone defined for the system: ::

    $ timedatectl [status]

To list available zones: ::

    $ timedatectl list-timezones

To set your time zone (This will create an ``/etc/localtime`` symlink that
points to a zoneinfo file under ``/usr/share/zoneinfo/``): ::

    # timedatectl set-timezone <Zone/SubZone>

    Equals to

    #  ln -sf /usr/share/zoneinfo/<Zone/SubZone> /etc/localtime

References
----------

``man timedatectl``

`Archwiki: system time
<https://wiki.archlinux.org/index.php/System_time>`_
