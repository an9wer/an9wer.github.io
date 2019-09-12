Deployment
==========

Fio
---

Fio Install
"""""""""""

::

    # yum install fio

Fio config
""""""""""

::

    [global]
    ioengine=libaio
    direct=1
    blocksize=1M
    iodepth=32
    verify=md5
    do_verify=1
    rw=write
    group_reporting

    [sda]
    filename=/dev/sda

    [sdb]
    filename=/dev/sdb

    ...

Fio Usage
"""""""""

::

    # fio <config file> --output <output file>

IPMI
----

IPMI Config
"""""""""""

Enter BIOS and scroll to IPMI menu:

::

    IPv4:    10.220.0.x
    Mask:    255.255.0.0
    Gateway: 10.0.0.8

IPMI Usage
""""""""""

Mount iso by samba:

::

    10.220.0.121
    \share\CentOS-7-x86_64-Minimal-1810.iso



Redfish
-------

nsd/storage/set-redfish-address.py

Redfish Requirements
""""""""""""""""""""

::

    # yum install sg3_utils
    # yum install python-ipaddress

Redfish Usage
"""""""""""""

Check enclosure dev:

::

    # lsscsi -g | grep enc

Set ip address of redfish server:

::

    # ./set-redfish-address.py --addr <address> --mask <mask> <dev>
    
Redfish API
"""""""""""

::

    # curl -k https://<domain>/redfish/v1


Iperf
-----

Iperf Installation
""""""""""""""""""

::

    # yum install iperf3

Iperf Usage
"""""""""""

Allow port:

::

    # firewall-cmd --add-port 5201/tcp

On node 1 (server):

::

    # iperf3 -s --internal 0 --verbose --logfile <logfile>

On node 2 (client):

::

    # iperf3 -c <ip> --internal 0 --verbose --logfile <logfile>


System Installation
-------------------

Erase superblock of disk:

::

    # dd if=/dev/zero of=/dev/sd<x> bs=1M count=1
