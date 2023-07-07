Troubleshooting Gentoo Update Problems 5 - Preserved Libraries
==============================================================

:Published: 2023/07/03

.. meta::
    :description: After updating Gentoo to the latest version, the system
        itself tells me to resolve the preserved library issue. What was that?

During my most recent update of Gentoo, the package *dev-libs/openssl* has been
updated from 1.1.1 to 3.0.9, as well as *dev-lang/python* from 3.10.10 to
3.11.4. For openssl, two shared library files have been renamed from xxx.so.1.1
to xxx.so.3. However, the problem was that there are two versions of Python
existed simultaneously in my current system. The old one based on the OpenSSL
1.1.1 is the Python 3.10.10, and the new one based on the Openssl 3.0.9 is the
Python 3.11.4.

Because of Gentoo's slotting feature [#]_, it is allowed to have different
versions of a package in the same system. However, I was curious of what Gentoo
actually do to allow different versions of a package based on different
versions of a library seperately.

Gentoo makes it possible by identifying and keeping the files from old packages
that are still in use in the current system. For instance, if listing all files
from the new OpenSSL package, the shared library files from the old OpenSSL
pacakge are shown in the output as well: ::

    $ equery files =dev-libs/openssl-3.0.9-r1
    ...
    /usr/lib64/libcrypto.so.1.1
    /usr/lib64/libcrypto.so.3
    /usr/lib64/libssl.so.1.1
    /usr/lib64/libssl.so.3
    ...

Next time when triggering the emerge command, I will be reminded to rebuild
old packages for applying new libraries. The file
*/var/lib/portage/preserved_libs_registry* also tells which old shared library
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

Therefore, the way to resolve that is by executing the following command to
rebuild old packages [#]_: ::

    $ sudo emerge --ask --verbose @preserved-rebuild

Or using a helper program ``revdev-rebuild`` to figure out what emerge command
should be used to deal with it [#]_: ::

    $ sudo revdep-rebuild --library /usr/lib64/libcrypto.so.1.1

Once done, the old version of Python will be updated to a new minor version
3.10.12. Since rebuilt, it is now based on the new version of OpenSSL. If
checking again all files belonging to the new OpenSSL package, no old shared
library files will be there: ::

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
