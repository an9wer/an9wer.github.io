.. meta::
    :robots: noindex

Glusterfs
=========

Types of Glusterfs daemon:

-   glusterd = management daemon
-   glusterfsd = per-brick daemon
-   glustershd = self-heal daemon
-   glusterfs = usually client-side, but also NFS on servers


Install glusterfs on CentOS7 (see https://wiki.centos.org/SpecialInterestGroup/Storage):

    ::

        # yum install centos-release-gluster6
        # yum install glusterfs-server


Quick start guide on CentOS7:

Have at least two nodes, format and mount all of them seperately:

::

    # mkfs.xfs /dev/<sdx>
    # mount /dev/<sdx> <mount point>

Before running `gluster` command, start *glusterd* on every nodes first:

::

    # systemctl start glusterd
    # systemctl enable glusterd

Configure trusted pool from nodes seperately:

::

    # gluster peer prob <server host/ip>

Create glusterfs volume from any single node:

::

    # gluster volume create <volume name> <volume type> <brick>...

From client, mount remote glusterfs volume:

::

    # mount -t glusterfs <brick> <mount point>


Command of gluster
------------------

List all volumes:

::

    # gluster volume list

Display information (i.e. brick name) of volumes (all if not specified):

::

    # gluster volume info [<volume>]


Display details/clients/memory of some brick of some volume:

::

    # gluster volume status <volume> <brick> detail|clients|mem


Create volume:

::

    # TODO

Start volume:

::

    # gluster volume start <volume>

Stop volume, add the option 'force' at the end if need to force stoping it:

::

    # gluster volume stop <volume> [force]


References:

-   `CentOS Wiki: gluster quickstart <https://wiki.centos.org/SpecialInterestGroup/Storage/gluster-Quickstart>`_

-   `Glusterfs Doc: quickstart <https://docs.gluster.org/en/latest/Quick-Start-Guide/Quickstart/>`_

