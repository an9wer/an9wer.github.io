.. meta::
    :robots: noindex

iptables
========

A package has three direction ways:

1. Destination local host (from outside to localhost)
2. Source local host (from localhost to outside)
3. Forwarded packets (between interfaces)

.. image:: /statics/images/notes/iptables.jpg
    :alt: iptables 

Delete rules of chain by rule number: ::

    # iptables -D <chain> <rulenum>

Extensions
----------

tcp
    These extensions can be used if ``--protocol tcp`` is specified: ::

        # iptables -A <chain> -p tcp --sport <source port>

udp
    These extensions can be used if ``--protocol udp`` is specified: ::

        # iptables -A <chain> -p upd --dport <destionation port>

Targets
-------

REDIRECT
    This target is only valid in the nat table, in the PREROUTING and OUTPUT
    chains, and user-defined chains which are only called from those chains.

    It redirects the packet to the machine itself by changing the destination
    IP to the primary address of the incoming interface (locally-generated
    packets are mapped to the localhost address, 127.0.0.1 for IPv4 and ::1 for
    IPv6): ::

        # iptables -t nat -A "PREROUTING|OUTPUT" -j REDIRECT --to-ports 1080

LOG
    The Linux kernel will print some information on all matching packets via
    the kernel log (where it can be read with ``dmesg`` or read in the syslog):
    ::

        # iptables -A <chain> -j LOG
    
References
----------

``man iptables``

``man iptables-extensions``

`iptables tutorial
<https://www.frozentux.net/iptables-tutorial/iptables-tutorial.html>`_
