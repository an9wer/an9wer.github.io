Linux SELinux
=============


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


`Fedora wiki: SELinux <https://fedoraproject.org/wiki/SELinux>`_
