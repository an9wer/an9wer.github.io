.. meta::
    :robots: noindex

Systemd hostnamectl
===================

See ``man hostnamectl``, ``man machine-info`` and `note of hostname
</notes/linux/hostname.html>`_.


Display current system hostname and related information: ::

    # hostnamectl [status]

Set HOSTNAME in */etc/hostname*: ::

    # hostnamectl set-hostname --static <hostname>

Set PRETTY_HOSTNAME in */etc/machine-info*: ::

    # hostnamectl set-hostname --pretty <hostname>

Reset hostname to its default (usually "localhost"): ::

    # hostnamectl set-hostname
    
Set CHASSIS in */etc/machine-info*: ::

    # hostname set-chassis <chassis>

Set DEPLOYMENT in */etc/machine-info*: ::

    # hostname set-deployment <deployment>
