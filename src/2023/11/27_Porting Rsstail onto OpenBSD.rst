Porting Rsstail onto OpenBSD
============================

:published: 2023-11-27

.. meta::
        :tags: OpenBSD

`Rsstail`_ is a command-line tool that monitors RSS feeds and detects new
entries. I found it as I was recently searching for a method to message me via
Telegram whenever there is a new post of `slashdot`_ published. Fortunately,
slashdot provides an RSS feed to notify readers know its updates, I can
integrate rsstail into a service that is run in the background to detect and
notify me of new entries of the RSS feed.

The service is supposed to run on an OpenBSD server, but rsstail has not been
ported onto OpenBSD, which means I have to build it by myself.

Build Libmrss
-------------

Since rsstail depends on `libmrss`_, the first step is to build libmrss.

The build process of libmrss relies on the automake and autoconf tool chains,
which can be installed through the ``pkg_add`` command on OpenBSD, and
while installing, select the latest version (i.e. automake-1.16.5 and
autoconf-2.71) for the prompt: ::

        $ doas pkg_add automake autoconf

Retrieve the source code of libmrss: ::

        $ git clone --depth 1 https://github.com/bakulf/libmrss

There is a "autogen.sh" file in the source code, which is the script to generate
a "configure" file. Note that the version of installed automake and autoconf
should be specified: ::

        $ AUTOMAKE_VERSION=1.16 AUTOCONF_VERSION=2.71 sh autogen.sh

After that, use the "configure" script to check dependent libraries and generate
a Makefile. Note that OpenBSD places files of a installed package, including
its library files if any, into the "/usr/local" directory (e.g.
"/usr/local/lib/libcurl.so"). To let the "configure" script find the location
of library files that is under the "usr/local" directory, use ``CPPFLAGS`` and
``LDFLAGS`` to specify the location expicitly : ::

        $ CPPFLAGS="-I/usr/local/include" LDFLAGS="-L/usr/local/lib" ./configure --prefix=/usr/local

Upon successful execution without any issues, a Makefile will be automatically
generated, and now we can compile the source code and install output files into
the system: ::

        $ make && make install

Build Rsstail
-------------

The next step is to build rsstail, which simpler than doing libmrss.

Retrieve the source code of rsstail: ::

        $ git clone --depth 1 https://github.com/folkertvanheusden/rsstail

The source code already includes a Makefile, but several minor modifications are
required: ::

        # add the "/usr/local" directory for the library search path
        $ sed -i -e '/^LDFLAGS=/ s/=/=-L\/usr\/local\/lib /' -e '/^CFLAGS=/ s/=/=-I\/usr\/local\/include /' Makefile

        # replace the library name of iconv
        $ sed -i '/^LDFLAGS=/ s/-liconv_hook/-liconv/' Makefile

        # change optimization level to 1
        $ sed -i '/^CFLAGS=/ s/-O3/-O1/' Makefile


Now that the Makefile has been modified, we can run the ``make`` command to
compile and install it: ::

        $ make && make install

Thanks for reading :)

.. _Rsstail: https://www.vanheusden.com/rsstail/
.. _slashdot: https://slashdot.org/
.. _libmrss: https://www.autistici.org/bakunin/codes.php#libmrss
