Sysctl
======

What is the difference between "all", "default" and a specific device in a
sysctl parameter?

**all**: If all sits in the device position of the parameter, all existing
devices will take on this specified parameter setting, regardless of the
interface's own setting. An exception would be that the interface value is a
greater than the 'all' value.

**default**: If default sits in the device position of the parameter, all
newly-created devices will take on this specified parameter setting

**ethX**: If ethX (any interface name) sits in the device position of the
parameter, only that device will take on this specified parameter setting

Example: ::

    net.ipv4.conf.all.rp_filter  = 1
    net.ipv4.conf.eth0.rp_filter = 0
    net.ipv4.conf.eth1.rp_filter = 0
    net.ipv4.conf.eth2.rp_filter = 2

Then ``eth0`` and ``eth1`` act as if ``rp_filter = 1``, ``eth2`` acts as if
``rp_filter = 2``. This is because all is set to 1, and the max value of all or
the interface name is used.

Variables
---------

route_localnet - BOOLEAN
    Do not consider loopback addresses as martian source or destination while
    routing. This enables the use of 127/8 for local routing purposes.  default
    FALSE

ip_forward - BOOLEAN
    Forward Packets between interfaces which makes it act like a router.

vm
--

swappiness

drop_caches
