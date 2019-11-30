Build raid1
===========

Create raid 1 device: ::

    # mdadm --create /dev/md1 --homehost=any --level=mirror --raid-devices=2 /dev/sda /dev/sdb

After that, check the process of creation command: ::

    # cat /proc/mdstat

Or use ``--detail`` option to get the state of raid device, if it contains
*resyncing*, then the creation is still being in work: ::

    # mdadm --detail /dev/md1
    State: clean, resyncing

References
----------

`Kernel wiki: raid setup
<https://raid.wiki.kernel.org/index.php/RAID_setup>`_
