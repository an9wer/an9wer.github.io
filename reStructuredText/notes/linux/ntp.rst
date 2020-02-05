Ntp
===

Install and setup on Archlinux: ::

    # pacman -S ntp

    # # Run at backgroud
    # systemctl start ntpd.service
    # systemctl enable ntpd.service
    or
    # # Run at boot time
    # systemctl start ntpdate.service
    # systemctl enable ntpdate.service

Install and setup on CentOS: ::

    # yum install ntp

    # # Run at backgroud
    # systemctl start ntpd.service
    # systemctl enable ntpd.service
    or
    # # Run manually
    # ntpdate 0.centos.pool.ntp.org

References
----------

`Wikipedia: ntp
<https://en.wikipedia.org/wiki/Network_Time_Protocol>`_

`Synchronize time with ntp
<https://www.tecmint.com/synchronize-time-with-ntp-in-linux/>`_

`Archwiki: ntpd
<https://wiki.archlinux.org/index.php/Network_Time_Protocol_daemon>`_

`How NTP Works
<https://www.eecis.udel.edu/~mills/ntp/html/warp.html>`_
