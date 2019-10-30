Linux network
=============

NIC (Network Interface Card) configuration file
-----------------------------------------------

Debian:

*man interfaces*

The traditional TCP/IP network setup on the Debian system uses ifupdown package
as a high level tool.

https://www.debian.org/doc/manuals/debian-reference/ch05.en.html


Fedora, RHEL, CentOS:

*man nm-settings-ifcfg-rh*

NetworkManager is based on the concept of connection profiles that contain
network configuration (see nm-settings(5) for details). The profiles can be
stored in various formats. NetworkManager uses plugins for reading and writing
the data. The plugins can be configured in NetworkManager.conf(5).

The ifcfg-rh plugin is used on the Fedora and Red Hat Enterprise Linux
distributions to read/write configuration from/to the traditional
/etc/sysconfig/network-scripts/ifcfg-* files.



Arch:

*man netctl.profile*

*netctl* is a CLI and profile-based network manager and an Arch project. 

https://wiki.archlinux.org/index.php/Netctl



DNS Search Domain
-----------------

`What is DNS search domain <https://askubuntu.com/a/574111>`_


CIDR
----

`Wikipedia: CIDR <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_


References
----------

`Wikipedia: TCP/IP <https://en.wikipedia.org/wiki/Internet_protocol_suite>`_

`Wikipedia: Link layer <https://en.wikipedia.org/wiki/Link_layer>`_

`Wikipedia: Network layer <https://en.wikipedia.org/wiki/Network_layer>`_
