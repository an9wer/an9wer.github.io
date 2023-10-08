The "Wrong" Way to Install OpenBSD (Draft)
==========================================

:published: 2023-10-02

.. meta::
	:tags: OpenBSD

This was my first time to install OpenBSD and my goal was to install it onto a
specfic partition of my disk, with some operating systems (Windows and Gentoo)
already installed on the other partitions. I thought the installation steps
should be as simple as what I did a few days ago for installing FreeBSD,
because in my mind they both are descendants of BSD (Berkeley Software
Distribution) and should be very similar for their installation. On the
contrary, I found it's not the case.

OpenBSD, in fact, provides a straightforward installation process through a
shell script that can be used by following all its prompts step by step to have
OpenBSD installed properly. However, there were two steps related to disk
partition making me confused at that time - editing partition tables (via
fdisk(8)) and creating disk labels (via disklabel(8)). If I did them wrong, even
a few mistakes only, I would ruin my entire disk including a Gentoo system that
I was using as my daily driver.

So I had to find a reliable method to install OpenBSD safely. The idea was
inspired by people using tools, such as ``dd``, to backup the whole system and
restore it on another disk. That means instead of making it happen directly on
the physical disk, I can first install it on a virtual disk (i.e. QEMU's raw
disk image) and then dump all its data onto the physical one.

Install on a Virtual Machine
----------------------------

Restore on a Physical Disk
--------------------------

Boot through UEFI
-----------------
