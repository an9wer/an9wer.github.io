EDC
===

Create cache disk: ::

    # pvcreate /dev/sdb /dev/sdc /dev/sdd
    # vgcreate vg_data /dev/sdb /dev/sdc /dev/sdd
    # lvcreate -n nginx -L 100g vg_data
    # lvcreate -n fstorage -l 100%Free vg_data
    # mkfs.xfs /dev/mapper/vg_data-nginx
    # mkfs.xfs /dev/mapper/vg_data-fstorage
    # mkdir /var/nginx
    # mkdir /nutstore
    # vim /etc/fstab
        /dev/mapper/vg_data-fstorage /nutstore          xfs     defaults 0 0
        /dev/mapper/vg_data-nginx /var/nginx            xfs     defaults 0 0
    # mount /var/nginx
    # mount /nutstore
