.. meta::
    :robots: noindex

Yum-utils
=========

::

    # yum install yum-utils


Download src.rpm: ::

    $ yumdownloader --source <package>

Unpack src.rpm: ::

    $ rpmd2cpio <package.src.rpm> | cpio -idmv

Extract spec file from src.rpm: ::

    $ rpm2cpio <package.src.rpm> | cpio -civ '*.spec'
