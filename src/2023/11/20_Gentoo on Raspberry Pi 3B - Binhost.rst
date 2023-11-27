Gentoo on Raspberry Pi 3B - Binhost
===================================

:published: 2023-11-20

.. meta::
        :tags: Gentoo RaspberryPi

In `my early post`_, a cross build environment has been set up on a powerful
AMD64 system to compile packages for the Raspberry Pi 3B. As mentioned, the
cross build environment itself is a minimal Linux root system, in which
armv7a-architecture packages are installed. However, how can those packages be
available to the Raspberry Pi 3B? Thus, in this post I will continue to set up a
binhost (binary package host) [#]_ on the AMD64 system, which aims to provide
the Raspberry Pi 3B readily installable, precompiled packages.

Set up a Binhost on the AMD64 System
------------------------------------

The first step is to generate binary packages whenever a package is installed by
the portage system, which can be approached by the ``buildpkg`` feature in
the "/etc/portage/make.conf" file: ::

	$ sudo nano /etc/portage/make.conf
		FEATURES="buildpkg"

Next step is to find a way of transfering binary packages from the AMD64 system
to the Raspberry Pi 3B. Here is an example of using the SSH protocol to access
binary packages: ::

	# copy the public key of the Raspberry Pi 3B to the AMD64 system
	$ ssh-copy-id -i ~/.ssh/rpi3b USER@AMD64


Install Binary Packages on the Raspberry Pi 3B
----------------------------------------------

Correspondingly, to let the portage system retreive binary packages while
installing packages is to use the ``getbinpkg`` feature in the
"/etc/portage/make.conf" file: ::

	$ sudo nano /etc/portage/make.conf
		FEATURES="getbinpkg"

Also, to tell the portage system to download binary packages through the SSH
protocol from the AMD64 system: ::

	$ sudo nano /etc/portage/make.conf
		PORTAGE_BINHOST="ssh://USER@AMD64/usr/armv7a-unknown-linux-gnueabihf/var/cache/binpkgs"

After that, installing a package on the Raspberry Pi 3B will not compile the
package from scratch, instead a pre-compiled binary package will be used: ::

	$ sudo emerge -av <PKG>

Thanks for reading :)

.. _my early post: /2023/11/18_Gentoo%20on%20Raspberry%20Pi%203B%20-%20Cross%20Compilation.html

Further Readings
----------------

.. [#] `Gentoo Wiki: Binary Package Guide <https://wiki.gentoo.org/wiki/Binary_package_guide>`_
