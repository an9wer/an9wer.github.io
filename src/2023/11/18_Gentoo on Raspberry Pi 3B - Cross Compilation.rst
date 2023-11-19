Gentoo on Raspberry Pi 3B - Cross Compilation
=============================================

:published: 2023-11-18

.. meta::
	:tags: Gentoo RaspberryPi

In `my last post`_, I have installed Gentoo on my Raspberry Pi 3B. However,
compiling packages from source codes (that is how Gentoo works) requires a lot
of hardware resources, it seems impractial to do that on a Raspberry Pi 3B.
Fortunately, it is possible to transfer the heavy compilation tasks to a
powerful AMD64 system (such as a Gentoo desktop/server with more compute cores
and more memory) using `crossdev`_  - a set of bash scripts that utilize emerge
to provide a system integrated cross-compilation capability.

Steps for Cross Compilation
---------------------------

Setup Cross-toolchain
"""""""""""""""""""""

Install the crossdev: ::

	$ sudo emerge -av sys-devel/crossdev

Install the toolchain for Raspberry Pi 3B in 32-bit mode: ::

	$ sudo crossdev --stable -t armv7a-unknown-linux-gnueabihf

The above command will create a cross build environment under the directory
"/usr/armv7a-unknown-linux-gnueabihf", which is a minimal root system: ::

	$ ls /usr/armv7a-unknown-linux-gnueabihf/
	bin  etc  lib  run  sbin  sys-include  tmp  usr  var

Such that we can cross compile packages and install them into the cross build
environment: ::

	$ sudo armv7a-unknown-linux-gnueabihf-emerge -av <PACKAGE>

But before installing any packages, we need to dive into the cross
build environment and configure its portage system.

Configure portage/make.conf
"""""""""""""""""""""""""""

Set FLAGS-related variables (just copied from the "make.conf" file in the
Raspberry Pi 3B): ::

	$ sudo nano /usr/armv7a-unknown-linux-gnuabihf/etc/portage/make.conf
		COMMON_FLAGS="-O2 -pipe -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard"
		CFLAGS="${COMMON_FLAGS}"
		CXXFLAGS="${COMMON_FLAGS}"
		FCFLAGS="${COMMON_FLAGS}"
		FFLAGS="${COMMON_FLAGS}"

Disable the ``introspection`` USE flag, because I found the
``gobject-introspection`` package `failed`_ to be cross compiled: ::

	$ sudo nano /usr/armv7a-unknown-linux-gnuabihf/etc/portage/make.conf
		USE="-introspection"

Configure portage/make.profile
""""""""""""""""""""""""""""""

The default "make.profile" in the cross build environment, created by the
crossdev, is linked to "gentoo/profiles/embedded". Here we set it to
"gentoo/profiles/default/linux/arm/17.0/armv7a" to keep it same as the one
in the Raspberry Pi 3B::

	$ sudo rm /usr/armv7a-unknown-linux-gnueabihf/etc/portage/make.profile
	$ sudo ln -s /var/db/repos/gentoo/profiles/default/linux/arm/17.0/armv7a /usr/armv7a-unknown-linux-gnueabihf/etc/portage/make.profile

Finally
-------

Now, we can cross compile packages for the Rapberry Pi 3B on a powerful AMD64
machine.

Thanks for reading :)

.. _my last post: /2023/11/12_Gentoo%20on%20Raspberry%20Pi%203B%20-%20Installation.html
.. _crossdev: https://wiki.gentoo.org/wiki/Crossdev
.. _failed: https://bugs.gentoo.org/850895
