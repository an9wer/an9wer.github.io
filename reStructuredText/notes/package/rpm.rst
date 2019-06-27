RPM
===

Query
-----

List all installed pacakges:

::

    $ rpm -qa

Display information og specified pacakge:

::

    $ rpm -qi <package_name>

List files of already installed pacakge:

::

    $ rpm -ql <package_file>

List files of specified RPM package:

::

    $ rpm -qlp <package_file>


Install
-------

Install pacakges:

::

    # rpm -i <package_file> [<package_file> ...]

Reinstall packages:

::

    # rpm -i --reinstall <package_file> [<package_file> ...]

