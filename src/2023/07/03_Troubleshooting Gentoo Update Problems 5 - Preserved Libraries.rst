Troubleshooting Gentoo Update Problems 5 - Preserved Libraries
==============================================================

:Published: 2023/07/03

.. meta::
    :description: After updating Gentoo to the latest version, the system
        itself tells me to resolve the preserved library issue. What was that?

During my most recent update, the package *dev-libs/openssl* has been updated
from 1.1.1 to 3.0.9, as well as *dev-lang/python* updated from 3.10.10 to
3.11.4. For openssl, two shared library files have been renamed from xxx.so.1.1
to xxx.so.3. However, because of Gentoo's slotting feature, my current system
has two versions of Python installed simultaneously, the old Python 3.10.10
built on the OpenSSL 1.1.1 and the new Python 3.11.4 built on the Openssl
3.0.9.

Gentoo makes it possible by identifying and keeping the files from old packages
that are still in use in the current system. For instance, after displaying all
files in the new OpenSSL package, it also shows shared library ifles from the
old OpenSSL pacakge: ::

    $ equery files =dev-libs/openssl-3.0.9-r1
    ...
    /usr/lib64/libcrypto.so.1.1
    /usr/lib64/libcrypto.so.3
    /usr/lib64/libssl.so.1.1
    /usr/lib64/libssl.so.3
    ...

Next time when triggering the emerge command, it will remind me to rebuild the
old package for applying new libraries. In the file
*/var/lib/portage/preserved_libs_registry*, it tells which old shared library
files are preserved: ::

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

The way to resolve that is executing the following command [#]_: ::

    $ sudo emerge --ask --verbose @preserved-rebuild

Or use a helper program ``revdev-rebuild`` [#]_: ::

    $ sudo revdep-rebuild --library /usr/lib64/libcrypto.so.1.1

After that, the old Python has been rebuilt on the new OpenSSL libraries and
updated to the new version 3.10.12. If checking again all files in the OpenSSL
package, I can find out the old shared library files has been removed: ::

    $ equery files =dev-libs/openssl-3.0.9-r1
    ...
    /usr/lib64/libcrypto.so.3
    /usr/lib64/libssl.so.3
    ...

Thanks for reading :)

References
----------
.. [#] `GentooWiki: Preserved Rebuild <https://wiki.gentoo.org/wiki/Preserved-rebuild>`_
.. [#] `GentooWiki: Preserve Libs <https://wiki.gentoo.org/wiki/Preserve-libs>`_
