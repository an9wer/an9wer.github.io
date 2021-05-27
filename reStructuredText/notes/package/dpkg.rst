.. meta::
    :robots: noindex

Dpkg
====

List files owned by installed packages: ::

    $ dpkg-query -L <package> [...]

List files owned by uninstalled pacakges: ::

    # apt install apt-file
    # apt-file update
    $ apt-file list <pattern>

