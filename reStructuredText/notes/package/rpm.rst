.. meta::
    :robots: noindex

RPM
===

Query
-----

List all installed pacakges: ::

    $ rpm -qa

Display information of specified installed pacakge: ::

    $ rpm -qi <package_name>

List files of already installed pacakge: ::

    $ rpm -ql <package_file>

List files of specified RPM package: ::

    $ rpm -qlp <package_file>


List reverse dependencies of package: ::

    $ rpm -q --whatrequires <package_name>


Install
-------

Install pacakges: ::

    # rpm -i <package_file> [<package_file> ...]

Reinstall packages: ::

    # rpm -i --reinstall <package_file> [<package_file> ...]

Misc
----

List all imported signing archive keys: ::

    # rpm -qa gpg-pubkey*

    Or

    # rpm -q gpg-pubkey --qf '%{NAME}-%{VERSION}-%{RELEASE}\t%{SUMMARY}\n'

Remove any unwanted archive signing keys: ::

    # rpm -e <gpg-pubkey-4da87d59-5ead3782>


References
----------

``man rpm``

``man rpmkeys``
