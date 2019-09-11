Deployment
==========

Fio
---

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



Mount





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
=====

Iperf Installation
""""""""""""""""""

::

    # yum install iperf3

Iperf Usage
"""""""""""

On node 1 (server):

::

    # iperf3 -s --internal 0 --verbose --logfile <logfile>

On node 2 (client):

::

    # iperf3 -c <ip> --internal 0 --verbose --logfile <logfile>

