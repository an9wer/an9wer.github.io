Build raid1
===========

Create raid1 array: ::

    # mdadm --create /dev/md1 --level=mirror --raid-devices=2 /dev/sda /dev/sdb

References
----------

`Kernel wiki: raid setup
<https://raid.wiki.kernel.org/index.php/RAID_setup>`_
