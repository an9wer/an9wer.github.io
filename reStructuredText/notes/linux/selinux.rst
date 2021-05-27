.. meta::
    :robots: noindex

Linux SELinux
=============

::

    # getenforce

::

    # setenforce [0|1]

::

    # sestatus

List available SELinux users:

::

    # seinfo -u

List available SELinux roles:

::

    # seinfo -r

::

    # semanage login -l

::

    # semanage permissive -l

::

    # semanage boolean -l

::

    # getsebool -a

::

    # setsebool -P httpd_can_network_connect_db on

SET Individual domains to permissive mode while the system runs in enforcing
mode. For example, to make the httpd_t domain permissive: 

::

    # semanage permissive -a httpd_t


::

    # chcon -t bin_t /usr/sbin/httpd 

Restores the default SELinux context for files:

::

    # restorecon -v /usr/sbin/httpd

TODO: aureport ausearch


References
----------

`Gentoo wiki: SELinux <https://wiki.gentoo.org/wiki/SELinux>`_
    Linux has a well-known discretionary access control (DAC) system, based on
    the permission mask set on resources and the ownership of the resource
    versus the run-time privileges of a process. Some additional security
    features are available as well, such as capabilities and extended ACLs,
    which allow administrators to fine-tune the secure state of their system.
    But even all those features still prove to be discretionary in their model. 

    A discretionary model means that the owner of a resource can still decide
    how the resource is shared on the system. A directory can be made
    world-writable by its owner, and from that point onward all processes on
    the system can write to the directory. With a mandatory access control
    system, the access to resources is governed through a mandatory system that
    cannot be worked around from. With SELinux, this is the SELinux security
    subsystem running in the Linux kernel. 

`Gentoo wiki: Introduction to SELinux <https://wiki.gentoo.org/wiki/SELinux/Quick_introduction>`_
    It is important to understand that the SELinux permission check happens
    after the Linux DAC check. In other words, SELinux cannot be used to
    override access controls on the system. 

    In SELinux, roles decide which types a process context can be in. The
    user_r role has the right to have processes run in the user_t type. Types
    for processes are also called **domains**. So the role-based access control
    decides which domains a role is allowed to have. 

    In permissive mode, SELinux will be consulted but will not enforce its
    decision. Instead, it will only log denials and still allow the action to
    continue. This is great for troubleshooting issues, as we can temporarily
    disable SELinux to see if it is really to blame, but also to convert a
    system to an SELinux system: we can verify that everything would work (no
    specific denials) after which we can enable SELinux.

`Gentoo wiki: SELinux users and logins <https://wiki.gentoo.org/wiki/SELinux/Users_and_logins>`_
    A Linux account is mapped to one (and only one) SELinux user, whereas a
    SELinux user can be linked to multiple roles. 

`Gentoo wiki: SElinux development <https://wiki.gentoo.org/wiki/Project:SELinux/Development>`_
    SELinux uses domains and types to differentiate its various security
    objects. A domain is usually referred to as the security context of a
    process (or group of processes) whereas a type is usually referred to as
    the label given to a particular resource (file, directory, network
    interface, socket, network port, ...).

    SELinux policies describe what interaction is allowed between a domain and
    the other domains and types it needs to work with. If no policy allows for
    a particular activity, then the activity is denied.

`Redhat doc: SELinux <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/selinux_users_and_administrators_guide/index>`_
    By default, newly-created files and directories inherit the SELinux type of
    their parent directories. 

`Fedora wiki: SELinux <https://fedoraproject.org/wiki/SELinux>`_
