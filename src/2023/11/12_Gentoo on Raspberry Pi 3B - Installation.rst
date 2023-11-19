Gentoo on Raspberry Pi 3B - Installation
========================================

:published: 2023-11-12

.. meta::
        :tags: Gentoo RaspberryPi

I have a Raspberry Pi 3B which I purchased around the year of 2017, but it was a
long time since I last powered it up. Superisingly, even after such a long
period of break, it still successfully booted up, and the system installed on it
reamined on an old version of Raspbian (based on Debian 10).

Why Raspberry Pi 3B?
--------------------

I reckon its hardware is relatively outdated and its performance is lower than
the lastest generation (i.e. Raspberry Pi 5), but I still have fun playing with
it. As an ARM-based single-board computer (SBC), it contains a quad-core ARMv8
(64-bit) CPU, which can also be operated in an ARMv7 compatible mode [#]_. That
means I can try either 32-bit or 64-bit systems on it. On the other hand, as a
popular SBC, it is supported widely by a lot of Linux distributions, even
OpenBSD's installation image can be booted on Raspberry Pi without any
additional modification.

Why Gentoo?
-----------

The reason why I choose Gentoo is that I want to try cross-compilation for ARM
chips. Gentoo is well-known for its package management system, which compiles
packages from source code, and it supports various CPU architectures, such as
ARM, RISC-V, SPARC, and etc. Also, I am using Gentoo as my daily driver, such
that I will not be juggling between different systems.

Steps for Installation
----------------------

Parpare a SD Card
"""""""""""""""""

Partition the SD Card, with two partitions: ::

	$ sudo fdisk /dev/sdX
		o		# a DOS-type partition table
		n +256M		# the partition for /boot
		n +left 	# the partition for /

Format the boot and root partitions respectively: ::

	$ sudo mkfs.vfat -F32 /dev/sdX1    # boot
	$ sudo mkfs.ext4 /dev/sdX2         # root

Mount the partitions into the system: ::

	$ sudo mount /dev/sdX2 /mnt        # root
	$ sudo mkdir /mnt/boot
	$ sudo mount /dev/sdX1 /mnt/boot   # boot

Install Root system
"""""""""""""""""""

Download Gentoo's stage3 archive files for Raspberry Pi 3B, which can be found
on its `download page`_, and unpack it into the root partition: ::

	# for example: the stage3 archive file for ARMv7a (32-bit) HardFP system with openrc
	# wget 'https://distfiles.gentoo.org/releases/arm/autobuilds/20231111T213157Z/stage3-armv7a_hardfp-openrc-20231111T213157Z.tar.xz'
	$ sudo tar xpvf stage3-armv7a_hardfp*.tar.xz --xattrs-include='*.*' --numeric-owner -C /mnt/

Install Bootloader and Linux Kernel
"""""""""""""""""""""""""""""""""""

The next step is to create the boot partition. According to the boot sequence of
Raspberry Pi 3B [#]_:

	1. The boot ROM is programmed into SoC during manufacturing of the RPI.
	This code looks for the file bootcode.bin in one of the partitions of
	SD card and executes it.

	2. The bootcode.bin code looks for the file config.txt for any third
	stage bootloader info. If nothing found, it loads the default bootloader
	start.elf from the SD card and runs it.

	3. The start.elf code reads config.txt multiple times to initialize
	basic hardware, load dtb and kernel into RAM.

The boot partition should include all files required for booting the system -
bootcode.bin, start.elf, device tree files, Linux kernel, and etc - all of those
can be downloaded from Raspberry Pi's `firmware repository`_ : ::

	$ git clone --depth 1 https://github.com/raspberrypi/firmware.git

Install them into the boot partition: ::

	$ sudo cp -r firmware/boot/* /mnt/boot

Also, kernel modules from Raspberry Pi's firmware repository should be stored
into the "lib" directory on the root partition: ::

	$ sudo cp -r firmware/modules /mnt/lib

Note that we can customize the boot options by creating the "config.txt"
and "cmdline.txt" files, although they are not provided by the firmware repository.

Create fstab
""""""""""""

Below is an example of an "/etc/fstab" file: ::

	UUID=C0D9-86FC                                  /boot   vfat    defaults                0 2
	UUID=7b511051-01a2-4dcc-8b71-d05200d57c4f       /       ext4    defaults,noatime        0 1

Install Firmware for Wifi and Bluetooth Chips
"""""""""""""""""""""""""""""""""""""""""""""

From now, insert the SD card into the Raspberry Pi 3B, and it would boot up
successfully. After initial boot, we need to install the firmware for Raspberry
Pi 3B's wifi and bluetooth chips.

The firmware for the wifi chip can be installed through emerge: ::

	$ sudo emerge -av sys-firmware/raspberrypi-wifi-ucode

The firmware for the bluetooth chip can be downloaded from Raspberry Pi's
`bluez-firmware repository`_: ::

	$ sudo mkdir -p /lib/firmware/brcm
	$ sudo wget -P /lib/firmware/brcm https://raw.githubusercontent.com/RPi-Distro/bluez-firmware/master/broadcom/BCM43430A1.hcd

Troubleshooting
---------------

Serial Port
"""""""""""

If it keeps returning the error message ``INIT: Id "s0" respawning too fast:
disabled for 5 minutes`` to the console, then enable uart: ::

	$ sudo nano /boot/config.txt
		enable_uart=1

Software Clock
""""""""""""""

The Raspberry Pi 3B doesn't have a hardware clock, while we can use a software
clock to mitigate the issue: ::

	# disable the hardware clock daemon
	$ sudo rc-update del hwclock boot
	# enable the software clock daemon
	$ sudo rc-update add swclock boot


Thanks for reading :)

Further Readings
----------------
.. [#] `Processing for Pi <https://pi.processing.org/technical/>`_
.. [#] `The boot sequence of Raspberry Pi 3 Model B <https://nayab.xyz/rpi3b-elinux/embedded-linux-rpi3-030-boot-process.html>`_

.. _download page: https://www.gentoo.org/downloads/#arm
.. _firmware repository: https://github.com/raspberrypi/firmware/tree/master
.. _bluez-firmware repository: https://github.com/RPi-Distro/bluez-firmware/tree/master
