Yum
===

**Note**: All of the following *glob_exp* is a package name which may contain
star (*) to match fuzzily, sometimes you need quote it ('*') or backslash it
(\*) to avoid bash expanding.

List
----

``yum list`` displays information on the version of the package, the format of
output is: ::

    name.arch [epoch:]version-release  repo or @installed-from-repo

**Note**: The repos of installed package are perfixed with '@' symbol.

List package(s) information from *all* (by default), *available to be
installed*, *availabe to be updated*, *installed* or *installed but not in yum
repository*: ::

    # yum list [all | available | updates | installed | extra ] [glob_exp ...]

List all/installed packages from speficied repo: ::

    # yum list "all|installed" | grep @<repo>

    or

    # yumdb search from_repo <repo>

Deplist
-------

List dependencies of packages: ::

    # yum deplist <package> [<package> ...]


Provides
--------

Find out which package provides a specific file or a file-glob-syntax
wildcards: ::

    # yum provides <file> [<file> ...]

    e.g.
    # yum provides /usr/bin/ps
    # yum provides '*/collectd2html.pl'


Group
-----

To view the number of installed groups, available groups, available environment
groups, and both installed and available language groups: ::

    # yum group summary


To list all package groups: ::

    # yum group list

To list language, environment, installed or availabe package groups: ::

    # yum group list [language | environment | installed | available]

To list packages contained in a particular group: ::

    # yum group info <glob_exp> [...]


-   " - ": Package is not installed and it will not be installed as a part of
    the package group.

-   " + ": Package is not installed but it will be installed on the next yum
    upgrade or yum group upgrade.

-   " = ": Package is installed and it was installed as a part of the package
    group.

-   "no symbol": Package is installed but it was installed outside of the
    package group. This means that the yum group remove will not remove these
    packages. 

To install package groups: ::

    # yum group install <glob_exp> [...]

To update package groups: ::

    # yum group update <glob_exp> [...]

To uninstall package groups: ::

    # yum group remove <glob_exp> [...]


References
----------

`Redhat Doc: Installing and Managing Software
<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/system_administrators_guide/index#part-Installing_and_Managing_Software>`_
