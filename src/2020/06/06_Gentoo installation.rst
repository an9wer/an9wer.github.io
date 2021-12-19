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

    # vi /mnt/gentoo/etc/portage/make.conf
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
    # emerge -av --newuse sys-kernel/linux-firmware

    2. Using distribution kernels
    # emerge --ask sys-kernel/installkernel-gentoo
    # emerge --ask sys-kernel/gentoo-kernel-bin
    # emerge -av --newuse sys-kernel/linux-firmware

Install network: ::

    1. Ethernet interface
    # emerge -av --newuse net-misc/netifrc
    # vim /etc/conf.d/net
        config_<interface>="dhcp"
    # ln -s /etc/init.d/net.lo /etc/init.d/net.<interface>
    # rc-update add net.<interface> default

    2. Wireless interface
    # emerge -av --newuse net-wireless/wpa_supplicant
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
    # emerge --ask x11-apps/xinit
    # emerge --ask x11-apps/xmodmap

Install fonts: ::

    # emerge --ask media-fonts/noto media-fonts/noto-cjk media-fonts/noto-emoji
    # emerge --ask media-fonts/ubuntu-font-family
    # emerge --ask media-fonts/fontawesome

Install dwm and st: ::

    # vim /etc/portage/package.use/dwm.use
        x11-terms/dwm savedconfig
    # emerge --ask x11-wm/dwm::an9wer

    # vim /etc/portage/package.use/st.use
        x11-terms/st savedconfig
    # emerge --ask x11-terms/st::an9wer

Install ibus: ::

    # vim /etc/portage/package.accept_keywords
        app-i18n/ibus-rime ~amd64
    # vim /etc/portage/package.use/ibus-rime.use
        app-i18n/ibus-rime extra
    # emerge --ask app-i18n/ibus app-i18n/ibus-rime
    # ibus-setup

    For ibus to work with Qt 5
    # vim /etc/portage/package.use/ibus.use
        dev-qt/qtgui dbus ibus
    # emerge --ask --oneshot --newuse dev-qt/qtgui

Install dunst: ::

    # emerge --ask x11-misc/dunst

Install redshift: ::

    # vim /etc/portage/package.use/redshift.use
        x11-misc/redshift geoclue
    # emerge --ask x11-misc/redshift

Install alsa: ::

    # vim /etc/portage/make.conf
        USE="alsa"
    # emerge --ask media-sound/alsa-utils
    
Install chroot: ::

    # mkdir /chroot
    # wget <PASTED_STAGE_URL>
    # tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner -C /chroot
    # mkdir -p /chroot/etc/portage/repos.conf
    # cp /etc/portage/repos.conf/gentoo.conf /chroot/etc/portage/repos.conf/gentoo.conf
    # cp --dereference /etc/resolv.conf /chroot/etc/
    # vim /etc/init.d/chroot
        name="chroot daemon"

        depend() {
           need localmount
           need bootmisc
        }

        start() {
             ebegin "Mounting chroot directories"
             mount -o rbind /dev /chroot/dev > /dev/null &
             mount -t proc none /chroot/proc > /dev/null &
             mount -o bind /sys /chroot/sys > /dev/null &
             mount -o bind /tmp /chroot/tmp > /dev/null &
             eend $? "An error occurred while mounting chroot directories"
        }

        stop() {
             ebegin "Unmounting chroot directories"
             umount -f /chroot/dev > /dev/null &
             umount -f /chroot/proc > /dev/null &
             umount -f /chroot/sys > /dev/null &
             umount -f /chroot/tmp > /dev/null &
             eend $? "An error occurred while unmounting chroot directories"
        }
    # rc-service chroot start
    # chroot /chroot /bin/bash
    # emerge-webrsync
    # exit

Install gnupg (use pinentry-gtk-2 to request the passphrase in a graphical
window): ::

    # vim /etc/portage/package.use/gnupg.use
        app-crypt/pinentry gtk
    # emerge --ask app-crypt/gnupg
    # eselect pinentry set pinentry-gtk-2

Install imagemagick: ::

    # vim /etc/portage/package.use/imagemagick.use
        media-gfx/imagemagick X
    # emerge --ask media-gfx/imagemagick

Install latex: ::

    # vim /etc/portage/package.use/texlive.use
        app-text/texlive cjk extra
    # emerge --ask app-text/texlive
    # emerge --ask dev-texlive/texlive-langchinese 


Updated 2021/04/04
------------------

如果想在 netifrc 中使用 dhcp 动态获取 ip 的同时，添加自己需要的 dns server（例
如 127.0.0.1），该怎么办？

可以通过安装 dhcpcd 并且在 netifrc 中指定使用 dhcpcd 作为 dhcp client 获取 ip： ::

    # emerge -av net-misc/dhcpcd
    # vim /etc/config/net
        modules="dhcpcd"

然后创建一个 */etc/resolv.conf.head* 文件，把自己需要的 dns server 填入： ::

    # vim /etc/resolv.conf.head
        nameserver 127.0.0.1

也可以是 */etc/resolv.conf.tail* 文件。 head 表示往 */etc/resolv.conf* 头部插入
，tail 表示往 */etc/resolv.conf* 后部插入。

Thanks for reading :)
