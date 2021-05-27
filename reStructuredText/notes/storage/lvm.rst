.. meta::
    :robots: noindex

LVM
===


Physical volume
---------------

There are three commands you can use to display properties of LVM physical
volumes: pvs, pvdisplay, and pvscan:

::

    # pvs

    # pvdiskplay

    # pvscan

Initialize physical volumes:

::

    # pvcreate /dev/sd<X> [...]


Volume group
------------

Add physical volumes to a volume group:

::

    # vgextend <volume group> <physical volume> [...]


Logical volume
--------------

Extend size of logical volume:

::

    # lvextend -l+100%FREE <logical volume>



    

Reference
---------

`Redhat 7: Logical Volume Manager Administration
<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/logical_volume_manager_administration/index>`_
