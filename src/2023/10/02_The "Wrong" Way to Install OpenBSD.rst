The "Wrong" Way to Install OpenBSD (Draft)
==========================================

:published: 2023-10-02

.. meta::
	:tags: OpenBSD

This was my first time to install OpenBSD and my goal was to install it onto a
specfic partition of my disk, with other operating systems (Windows and Gentoo)
already installed on the other partitions. I thought the installation steps
should be as simple as what I did a few days ago for installing FreeBSD, because
they both are descendants of BSD (Berkeley Software Distribution) and in my
mind they should be similar. On the contrary, I found it's quite challenging.

Actually, OpenBSD provides an easy way for its installation - a shell script
that I can use by following all the prompts step by step to have OpenBSD
installed properly on my disk. However, there were two steps related to dealing
with disks that made me confused at that time - editing partition tables (via
fdisk(8)) and creating disk labels (via disklabel(8)). If I did these two steps
wrong, even a few mistakes only, I would ruin my entire disk including the
current operating system that I was using.

So I needed to find a safe method to install OpenBSD.
