Yum
===

list
----

``yum list`` displays information on the version of the package, the format of
output is:

::

    name.arch [epoch:]version-release  repo or @installed-from-repo


List package(s) information from all (by default), available to be installed,
availabe to be updated, installed, installed but not in yum repository listed
in config file packages:

::

    # yum list [all | available | updates | installed | extra ] [glob_exp ...]

*glob_exp* is a package name which may contain star (*) to match fuzzily,
sometimes you need quote it to avoid bash expanding.

deplist
-------



