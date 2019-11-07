Linux hostname
==============

See ``man 1 hostname``, ``man 5 hostname``, ``man 7 hostname``.

To set the hostname, edit */etc/hostname* to include a single line with
<hostname>: ::

    # vim /etc/hostname
    <hostname>
    # reboot

Alternatively, using ``hostnamectl``: ::

    # hostnamectl set-hostname --static <hostname>
    # reboot


To temporarily set the hostname, use ``hostname``: ::

    # hostname <hostname>
    # exec bash -l
