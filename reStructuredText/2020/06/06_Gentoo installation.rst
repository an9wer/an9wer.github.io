Gentoo installation
===================

Prepare
-------

Setup network: ::

    # net-setup

format disk: ::

    1. UEFI + GPT
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
    # mkfs.ext4 /dev/sda3
    # mount /dev/sda3 /mnt/gentoo

    2. BIOS + MBR
    # fdisk /dev/sda
        o
        n +128M     # for /boot
        n +512M     # for swap
        n +remain   # for /
        t 1 83      # Linux
        t 2 82      # Linux swap
        t 3 83      # Linux
    # mkfs.ext2 -T small /dev/sda1
    # mkswap /dev/sda2
    # swapon /dev/sda2
    # mkfs.ext4 -T small /dev/sda3
    # mount /dev/sda3 /mnt/gentoo
    
Synchronize system time: ::

    # ntpd -q -g

Install stage tarball: ::

    # cd /mnt/gentoo
    # wget <PASTED_STAGE_URL>
    # tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner

Configure portage: ::

    # nano -w /mnt/gentoo/etc/portage/make.conf
        MAKEOPTS="-j5"
        GENTOO_MIRRORS="https://mirrors.tuna.tsinghua.edu.cn/gentoo https://mirrors.163.com/gentoo/"

    # mkdir --parents /mnt/gentoo/etc/portage/repos.conf
    # cp /mnt/gentoo/usr/share/portage/config/repos.conf /mnt/gentoo/etc/portage/repos.conf/gentoo.conf
    # cp --dereference /etc/resolv.conf /mnt/gentoo/etc/

Mounting the necessary filesystems: ::

    # mount --types proc /proc /mnt/gentoo/proc
    # mount --rbind /sys /mnt/gentoo/sys
    # mount --make-rslave /mnt/gentoo/sys
    # mount --rbind /dev /mnt/gentoo/dev
    # mount --make-rslave /mnt/gentoo/dev 

System Installation
-------------------

Chroot: ::

    # chroot /mnt/gentoo /bin/bash 
    # source /etc/profile
    # mount /dev/sda1 /boot

Install basic packages: ::

    # emerge-webrsync
    # eselect profile list
    # emerge --ask --verbose --update --deep --newuse @world

Set timezone: ::

    # echo "Asia/Shanghai" > /etc/timezone
    # emerge --config sys-libs/timezone-data

Synchronize the system clock : ::

    # emerge --ask net-misc/chrony
    # rc-update add chronyd default

Set locale: ::

    # echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
    # locale-gen
    # eselect locale list
    # eselect locale set <number>
    # env-update && source /etc/profile

Install kerenl: ::

    1. Using genkernel
    # emerge --ask sys-kernel/gentoo-sources
    # emerge --ask sys-kernel/genkernel
    # nano -w /etc/fstab    # if /boot is at a seperate disk
        /dev/sda1   /boot   ext2    defaults    0 2
    # genkernel all
    # emerge --ask sys-kernel/linux-firmware

    2. Using distribution kernels
    # emerge --ask sys-kernel/installkernel-gentoo
    # emerge --ask sys-kernel/gentoo-kernel-bin

Install network: ::

    1. Ethernet interface
    # emerge --ask net-misc/netifrc
    # vim /etc/conf.d/net
        config_<interface>="dhcp"
    # ln -s /etc/init.d/net.lo /etc/init.d/net.<interface>
    # rc-update add net.<interface> default

    2. Wireless interface
    # emerge --ask net-wireless/wpa_supplicant
    # vim /etc/wpa_supplicant/wpa_supplicant.conf
        # Allow users in the 'wheel' group to control wpa_supplicant
        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel

        # Make this file writable for wpa_gui / wpa_cli
        update_config=1

        network={
          ssid="<SSID>"
          psk="<PSK>"
        }
    # vim /etc/conf.d/net
        modules_<wlan>="wpa_supplicant"
        config_<wlan>="dhcp"
    # cp /etc/init.d/net.lo /etc/init.d/net.<wlan>
    # rc-update add net.<wlan> default

Install syslog: ::

    # emerge --ask app-admin/sysklogd
    # rc-update add sysklogd default

Install bootloader: ::

    1. BIOS and MBR
    # emerge --ask --verbose sys-boot/grub:2
    # grub-install /dev/sda
    # grub-mkconfig -o /boot/grub/grub.cfg

    2. UEFI and GPT
    # echo 'GRUB_PLATFORMS="efi-64"' >> /etc/portage/make.conf
    # emerge --ask sys-boot/grub:2
    # grub-install --target=x86_64-efi --efi-directory=/boot --removable
    # grub-mkconfig -o /boot/grub/grub.cfg

Application installation
------------------------

Install cpupower: ::

    # emerge --ask sys-power/cpupower

Install xorg: ::

    https://wiki.gentoo.org/wiki/Elogind
    # vim /etc/portage/make.conf
        USE="elogind -consolekit -systemd"
    # emerge --ask --changed-use --deep @world
    # rc-update add dbus default
    # reboot

    # vim /etc/portage/make.conf
        INPUT_DEVICES="libinput synaptics"
        VIDEO_CARDS="intel"
    # emerge --ask x11-base/xorg-server
