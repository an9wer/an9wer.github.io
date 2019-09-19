Deployment
==========

IPMI
----

Enter BIOS, scroll to IPMI menu and set:

::

    IPv4:    10.220.0.x
    Mask:    255.255.0.0
    Gateway: 10.0.0.8

Mount iso by samba:

::

    10.220.0.121
    \share\CentOS-7-x86_64-Minimal-1810.iso


System Installation
-------------------

Erase superblock of disk:

::

    # dd if=/dev/zero of=/dev/sd<x> bs=1M count=1

::

    Select two disks:
    /boot   1G      xfs     raid1
    /       80G     xfs     lvm raid1

Fio
---

Fio installation:

::

    # yum install fio

Fio configuration:

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

::

    # fio <config file> --output <output file>

Smartctl
--------

Smartctl installation

::

    # yum install smartmontools

Smartctl usage:

::

    # smartctl -a /dev/sd<x>

Useful parameters of HDD:

::

    1   Raw_Read_Error_Rate     0
    5   Realloacated_Sector_Ct  0
    7   Seek_Error_Rate         0
    196 Reallocated_Event_Count 0
    197 Current_Pending_Sector  0

Check intel SDD:

::

    # nsd/configuration/puppet/modules/nagios/files/plugins/check_intel_ssds 

Redfish
-------

Install Requirements

::

    # curl http://sg.danny.cz/sg/p/sg3_utils-1.42-1.x86_64.rpm -o sg3_utils-1.42-1.x86_64.rpm
    # curl http://sg.danny.cz/sg/p/sg3_utils-libs-1.42-1.x86_64.rpm -o sg3_utils-libs-1.42-1.x86_64.rpm
    # yum install sg3_utils-1.42-1.x86_64.rpm sg3_utils-libs-1.42-1.x86_64.rpm
    # yum install python-ipaddress

Check enclosure dev:

::

    # lsscsi -g | grep enc

Set ip address of redfish server:

::

    # nsd/storage/set-redfish-address.py --addr <address> --mask <mask> <dev>

Change administrator's password of redfish server:

::

    # curl -X PATCH --basic -v https://<ip>/redfish/v1/AccountService/Accounts/1 -H 'content-type: application/json; charset=utf-8' -u admin:admin --insecure -d '{"Password" : "adminadmin"  }'

    
Redfish api:

::

    # curl -k https://<domain>/redfish/v1


Redfish update firmware:

::

    # sg_ses_microcode /dev/sg<X> -m 0xe -N -b 4096 -I <filename> -vv

Iperf
-----

Iperf Installation:

::

    # yum install iperf3

Allow port of iperf server in iptables:

::

    # firewall-cmd --add-port 5201/tcp

On node 1 (server):

::

    # iperf3 -s -B <server ip> --internal 0 --verbose --logfile <logfile>

On node 2 (client):

::

    # iperf3 -c <server ip> --internal 0 --time 50000 --verbose --logfile <logfile>


Puppet
------

Puppet installation:

::

    # fab -f nsd/configuration/fabfile.py -u root -I -H <hostname>[,<hostname>,...] install_puppet run_agent:noop=False
