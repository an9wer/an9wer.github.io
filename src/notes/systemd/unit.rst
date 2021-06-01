.. meta::
    :robots: noindex

Systemd unit
============

A unit file is a plain text ini-style file that encodes information about a
service, a socket, a device, a mount point, an automount point, a swap file or
partition, a start-up target, a watched file system path, a timer controlled
and supervised by systemd, a resource management slice or a group of externally
created processes.

Unit section
------------
"[Unit]" section carries generic information about the unit that is not
dependent on the type of unit.

Install section
---------------

"[Install]" section carries installation information for the unit. This section
is not interpreted by systemd during runtime; it is used by the enable and
disable commands of the systemctl tool during installation of a unit.



References
----------

``man systemd.unit``
