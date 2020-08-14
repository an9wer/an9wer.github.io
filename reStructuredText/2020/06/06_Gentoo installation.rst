Gentoo installation
===================

::

    # net-setup
    # fdisk /dev/sda
        g
        n +128M     # for /efi
        n +16G      # for swap
        n +remain   # for /
        t 1 1       # for EFI System
        t 2 19      # for Linux swap
        t 3 20      # for Linux filesystem
        w           # write
    # mkfs.fat -F32 /dev/sda1
    # mkswap /dev/sda2
    # swapon /dev/sda2
    # mkfs.ext4 -T small /dev/sda3
    # mount /dev/sda3 /mnt/gentoo
    
::

    # ntpd -q -g

::

    # cd /mnt/gentoo
    # wget <PASTED_STAGE_URL>
    # tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner



::

    # nano -w /mnt/gentoo/etc/portage/make.conf
        MAKEOPTS="-j5"
        GENTOO_MIRRORS="https://mirrors.tuna.tsinghua.edu.cn/gentoo https://mirrors.163.com/genntoo/"

::

    # mkdir --parents /mnt/gentoo/etc/portage/repos.conf
    # cp /mnt/gentoo/usr/share/portage/config/repos.conf /mnt/gentoo/etc/portage/repos.conf/gentoo.conf
    # cp --dereference /etc/resolv.conf /mnt/gentoo/etc/


    # mount --types proc /proc /mnt/gentoo/proc
    # mount --rbind /sys /mnt/gentoo/sys
    # mount --make-rslave /mnt/gentoo/sys
    # mount --rbind /dev /mnt/gentoo/dev
    # mount --make-rslave /mnt/gentoo/dev 

::

    # chroot /mnt/gentoo /bin/bash 
    # source /etc/profile
    # mount /dev/sda1 /boot

::

    # emerge-webrsync
    # eselect profile list
    # emerge --ask --verbose --update --deep --newuse @world


::

    # echo "Asia/Shanghai" > /etc/timezone
    # emerge --config sys-libs/timezone-data

::

    # echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
    # locale-gen
    # eselect locale list
    # eselect locale set <number>
    # env-update && source /etc/profile

::

    # emerge --ask sys-kernel/gentoo-sources
    # emerge --ask sys-kernel/genkernel
    # nano -w /etc/fstab
        /dev/sda1   /boot   ext2    defaults    0 2
    # genkernel all
    # emerge --ask sys-kernel/linux-firmware
