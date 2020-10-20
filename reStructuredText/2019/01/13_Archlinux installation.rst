Archlinux installation
======================

Flash iso
---------

::

    $ dd if=archlinux-{x}-x86_64.iso of=/dev/sd{x} status="progress"

System installation
-------------------

Partition and mount: ::

    wifi-menu
    timedatectl set-ntp true
    fdisk /dev/sda
        g
        n +512M     # for /efi
        n +8192M    # for swap
        n +remain   # for /
        t 1 1       # for EFI System
        t 2 19      # for Linux swap
        t 3 20      # for Linux filesystem
        w           # write

    mkfs.fat -F32 /dev/sda1
    mkswap /dev/sda2
    swapon /dev/sda2
    mkfs.ext4 /dev/sda3

    mount /dev/sda3 /mnt
    mkdir /mnt/efi
    mount /dev/sda1 /mnt/efi

    pacstrap /mnt base linux linux-firmware base-devel vim

    genfstab -U /mnt >> /mnt/etc/fstab

    arch-chroot /mnt


Datetime: ::

    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    hwclock --systohc


Locale: ::

    vim /etc/locale.gen
        uncomment en_US.UTF-8 UTF-8
    locale-gen
    vim /etc/locale.conf
        LANG=en_US.UTF-8


Hostname: ::

    vim /etc/hostname
        peace


Network
"""""""

Use NetworkManager: ::

    pacman -S networkmanager
    systemctl enable NetworkManager

Or use systemd-network: ::

    vim /etc/systemd/network/<nic>.network
        [Match]
        Name=<nic>
     
        [Network]
        DHCP=ipv4
        EOF
    systemctl enable systemd-networkd
    systemctl enable systemd-resolved
    ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf


User account
""""""""""""

Create user: ::

    useradd -m -g wheel an9wer
    passwd an9wer
    visudo
        uncomment %wheel ALL=(ALL) NOPASSWD: ALL
        useradd -m -g wheel an9wer
        passwd an9wer


Bootloader
""""""""""

EFI Bootloader: ::

    pacman -S grub efibootmgr
    grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=archlinux
    grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=archlinux --removable
    grub-mkconfig -o /boot/grub/grub.cfg

Legency Bootloader: ::
    
    pacman -S grub
    grub-install --target=i386-pc /dev/sda
    grub-mkconfig -o /boot/grub/grub.cfg


Exit and reboot: ::

    exit
    umount -R /mnt

    reboot

Application installation
------------------------

Update system: ::

    sudo pacman -Syu


Install xorg: ::

    sudo pacman -S xorg xorg-xinit
        xorg, which contains xorg-server, is needed by dwm and i3.


Install suckless tools: ::

    sudo pacman -S libx11 libxft libxinerama

    git clone https://git.suckless.org/dwm
    make && sudo make install

    git clone https://git.suckless.org/st
    make && sudo make install


Install fonts: ::

    sudo pacman -S adobe-source-code-pro-fonts ttf-ubuntu-font-family ttf-font-awesome
        for terminal
    sudo pacman -S noto-fonts noto-fonts-cjk
        for firefox

Install virtual console font: ::

    sudo pacman -S tamsyn-font terminus-font


Install firefox: ::

    sudo pacman -S firefox flashplugin
        Preferences->General->Fonts:
            Serif: Noto Serif
            Sans-serif: Noto Sans
            Monospace: Noto Sans Mono

Install chromium: ::

    sudo pacman -S chromium


Install basic tools: ::

    sudo pacman -S openssh
    sudo pacman -S bash-completion
    sudo pacman -S shadowsocks-qt5

    sudo pacman -S xdg-user-dirs
        xdg-user-dirs-update


Install alsa: ::

    sudo pacman -S alsa-utils
        amixer sset Master unmute

Install dunst: ::

    sudo pacman -S dunst libnotify


Install fcitx: ::

    sudo pacman -S fcitx fcitx-im fcitx-configtool
        run 'fcitx-configtool'

Install ibus: ::

    $ sudo pacman -S ibus ibus-rime
    $ ibus-setup

Install mupdf: ::

    sudo pacman -S mupdf-gl
        if some error of OpenGL happens, may need to install the appropriate dirver for graphic card.
            sudo pacman -S nvidia*


Install imagemagick: ::

    sudo pacman -S imagemagick


Install telegram: ::

    sudo pacman -S telegram-desktop


Install virtualbox: ::

    sudo pacman -S virtualbox
        When encounter "Kernel driver not installed (rc=-1908)"
            sudo modprobe vboxdrv
        When encounter the problem about Mouse disappearing
            https://superuser.com/a/1390258


Bluetooth: ::

    sudo pacman -S pulseaudio pluseaudio-bluetooth bluez bluez-utils
        restart pulseaudio
            pulseaudio --kill
            pulseaudio --start
        run bluetoothctl to connect device


Fix tap-to-click for touchpad: ::

    sudo pacman -S xf86-input-synaptics
       synclient TapButton1=1 TapButton2=3 TapButton3=2


Update 2019/03/25
-----------------

When installing archlinux on ACER, encounter secure boot problem. Find a
way to solve it: https://itsfoss.com/no-bootable-device-found-ubuntu/

Update 2019/04/26
-----------------

Disable nvidia graphic card: ::

    sudo pacman -S bumblebee bbswitch
    sudo pacman -S xf86-video-intel (I don't know is this pacakge required?)

    vim /etc/modules-load.d/bbswitch.conf
        bbswitch

    vim /etc/modprobe.d/bbswitch.conf
        options bbswitch load_state=0 unload_state=1

    vim /etc/X11/xorg.conf.d/20-intel.conf
        Section "Device"
            Identifier  "Intel Graphics"
            Driver      "intel"
        EndSection

    vim /etc/X11/xorg.conf.d/20-monitor.conf
        Section "Monitor"
            Identifier  "HDMI1"
        EndSection
        Section "Monitor"
            Identifier  "eDP1"
            Option      "LeftOf" "HDMI1"
        EndSection

    Then, reboot, run command `lspci -k` to check that the kernel driver of 3D
    controller is not in use.


Update 2019/05/02
-----------------

Set tap button of touchpad: ::

    vim /etc/X11/xorg.conf.d/70-synaptics.conf
        Section "InputClass"
            Identifier "touchpad"
            Driver "synaptics"
            MatchIsTouchpad "on"
                Option "TapButton1" "1"
                Option "TapButton2" "3"
                Option "TapButton3" "2"
        EndSection


Update 2019/10/16
-----------------

Install RDP client remmina: ::

    # pacman -S remmina freerdp

Update 2020/08/19
-----------------

Disable the root login: ::

    # passwd -l root

Unlock root: ::

    $ sudo passwd -u root

https://wiki.archlinux.org/index.php/Sudo#Disable_root_login

