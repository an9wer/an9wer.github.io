Mdadm
=====

Deactivate raid device: ::

    # mdadm --stop <raid device>

Print details of raid device: ::

    # mdadm --detail <raid device>

Print metadata of component of raid device (see `difference between
--examine and --detail`_): ::

    # madadm --detail <device>

To load raid device automatically: ::

    # mdadm --assemble --scan

To load raid device manually if above command doesn't work (see `errors may
happen when loading raid device manually`_): ::

    # mdadm --assemble <raid device> <device> [<device> ...]

Remove a device from array of raid device: ::

    # mdadm --manage <raid device> --remove <device>

Add a deivce to array of raid device: ::

    # mdadm --manage <raid device> --add <device>

Update name, homehost or any other parameter of raid device: ::

    Stop raid device first
    # mdadm --stop <raid device>

    Update name
    # mdadm --assemble --update name --name <name> <raid device> <device> [<device>]

    Or update homehost (The special name "any" can be used as a wild card)
    # mdadm --assemble --update homehost --homehost <homehost> <raid device> <device> [<device>]


.. _difference between --examine and --detail:

-   defference between --examine and --detail

    ``--examine`` applies to devices which are components of an array, while
    ``--detail`` applies to a whole array which is currently active.

.. _errors may happen when loading raid device manually:

-   errors may be happened when loading raid device manually:

    Case1: Fewer devices are given than when they are created before, then use
    ``--run`` option: ::

        # mdadm --assemble /dev/md1 /dev/sdb
        mdadm: /dev/md1 assembled from 1 drive - need all 2 to start it (use --run to insist).

        Use --run option
        # mdadm --assemble --run /dev/md1 /dev/sdb

        Check the state of raid device which has 'degraded' now
        # mdadm --detail /dev/md1
        State : clean, degraded

    Case2: Some device is busy, then stop the hidden raid device first: ::

        # mdadm --assemble /dev/md1 /dev/sdb /dev/sdc
        mdadm: /dev/sdb is busy - skipping

        Find the hidden raid device
        # cat /proc/mdstat
        Personalities :
        md127 : inactive sdb[1](S)
        7982080 blocks super 1.2

        Stop the hidden raid device
        # mdadm --stop /dev/md127
        mdadm: stopped /dev/md127

