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

Steps to Install
----------------

Parpare a SD card, and partition it: ::

	$ sudo fdisk /dev/sdX
		o		# a DOS-type partition table
		n +256M		# the partition for /boot
		n +left 	# the partition for /

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
can be downloaded under Raspberry Pi's `firmware repository`_ : ::

	$ sudo mkfs.vfat -F32 /dev/sdX1
	$ sudo mount /dev/sdX1 /mnt

	$ git clone https://github.com/raspberrypi/firmware.git
	$ sudo cp -r firmware/boot/* /mnt

	$ sudo umount /dev/sdX1

Note that we can customize the boot options by creating the files config.txt
and cmdline.txt, which are not provided by the firmware repository.

Next, create the root partition. As Gentoo offers stage3 archive files, which
can be found in its `download page`_, we can simply decompress them into the
root partition: ::

	$ sudo mkfs.ext4 /dev/sdX2
	$ sudo mount /dev/sdX2 /mnt

	$ # download stage3 archive file for ARMv7a (HardFP)
	$ sudo tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner -C /mnt/

Also, kernel modules from Raspberry Pi's firmware repository should be stored
into the root partition: ::

	$ git clone https://github.com/raspberrypi/firmware.git
	$ sudo cp -r firmware/modules /mnt/lib

	$ sudo unmount /dev/sdX2

After that, insert SD card into the Raspberry Pi 3B, and it would boot up
successfully.

After Boot
----------

The firmware for the wifi chips on the Raspberry Pi 3B was missed and can be
installed through: ::

	$ sudo emerge -av sys-firmware/raspberrypi-wifi-ucode

Thanks for reading :)

Further Readings
----------------
.. [#] `Processing for Pi <https://pi.processing.org/technical/>`_
.. [#] `The boot sequence of Raspberry Pi 3 Model B <https://nayab.xyz/rpi3b-elinux/embedded-linux-rpi3-030-boot-process.html>`_

.. _firmware repository: https://github.com/raspberrypi/firmware/tree/master
.. _download page: https://www.gentoo.org/downloads/#arm
