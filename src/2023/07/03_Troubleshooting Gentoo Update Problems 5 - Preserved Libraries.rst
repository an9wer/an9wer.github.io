Troubleshooting Gentoo Update Problems 5 - Preserved Libraries
==============================================================

:Published: 2023/07/03

.. meta::
    :description: During the update of Gentoo, it shown me to resolve the
        preserved library issue.

During my recent update of Gentoo, the package *dev-libs/openssl* was updated
from 1.1.1 to 3.0.9, as well as two of its shared library files renamed from
"xxx.so.1.1" to "xxx.so.3". The problem was that there were two versions of
Python existed simultaneously on my system. The old version was Python 3.10.10,
which was based on the OpenSSL 1.1.1, and the new version was Python
3.11.4, based on the Openssl 3.0.9.

Gentoo allows different versions of the same package existed at the same time
beecause of its slotting feature [#]_. But what magic does Gentoo use to let
different versions of a package rely on different versions of a library
seperately? And what if the old version of the library package has been removed?

The answer is that gentoo will identify what files of the old version are still
in use and then keep them in the new version. For instance, if listing all files
in the new OpenSSL package, the shared library files from the old version
of OpenSSL can be found in the output as well: ::

    $ equery files =dev-libs/openssl-3.0.9-r1
    ...
    /usr/lib64/libcrypto.so.1.1
    /usr/lib64/libcrypto.so.3
    /usr/lib64/libssl.so.1.1
    /usr/lib64/libssl.so.3
    ...

However, next time when the emerge command was executed, it will remind you to rebuild
packages that were built on the old version of libraries with the new ones. A
special file */var/lib/portage/preserved_libs_registry* is used by Gentoo
to records what old files are preserved. It should be empty if there is no
preserved librariy issue: ::

    {
      "dev-libs/openssl:0": [
        "dev-libs/openssl-3.0.9-r1",
        "1067",
        [
          "/usr/lib64/libcrypto.so.1.1",
          "/usr/lib64/libssl.so.1.1"
        ]
      ]
    }

The way to resolve such problem is by executing the following command to rebuild
old packages [#]_: ::

    $ sudo emerge --ask --verbose @preserved-rebuild

Or by using a helper program ``revdev-rebuild`` to figure out what emerge
command should be used to solve it [#]_: ::

    $ sudo revdep-rebuild --library /usr/lib64/libcrypto.so.1.1

Once done, Python will be updated to a new version, which is 3.10.12. Since
rebuilt, it is now based on the new version of OpenSSL, and if checking again
all files in the new package of OpenSSL, old shared library files will not be
there any more: ::

    $ equery files =dev-libs/openssl-3.0.9-r1
    ...
    /usr/lib64/libcrypto.so.3
    /usr/lib64/libssl.so.3
    ...

Thanks for reading :)

References
----------
.. [#] `GentooWiki: Slotting <https://devmanual.gentoo.org/general-concepts/slotting/index.html>`_
.. [#] `GentooWiki: Preserved Rebuild <https://wiki.gentoo.org/wiki/Preserved-rebuild>`_
.. [#] `GentooWiki: Preserve Libs <https://wiki.gentoo.org/wiki/Preserve-libs>`_
