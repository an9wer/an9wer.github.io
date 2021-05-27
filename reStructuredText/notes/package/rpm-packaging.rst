.. meta::
    :robots: noindex

Package rpm-packaging
=====================

Using proxy if needed: ::

    Fedora:
    # vim /etc/dnf/dnf.cnf
        proxy=http://<ip>:<port>

    CentOS
    # vim /etc/dnf/dnf.cnf
        proxy=socks5://<ip>:<port>

Install required packages: ::

    Fedora:
    # dnf install rpm-build rpmdevtools

    CentOS
    # yum install rpm-build rpmdevtools

Create required directory structure in home directory: ::

    # rpmdev-setuptree

Install build dependencies: ::

    Fodora
    # dnf builddep <spec file>
    # dnf buildep <src rpm file>

    CentOS
    # yum-builddep <spec file>
    # yum-builddep <src rpm file>

Download source files: ::

    $ spectool -g -R <spec file>

    Or

    $ rpmbuild --undefine=_disable_source_fetch -ba <spec file>

Download rpm: ::

    Fedora
    # dnf download <package>

    CentOS
    # yum install yum-utils
    # yumdownloader <package>

Download src rpm: ::

    Fedora
    # dnf download --source <package>

    CentOS
    # yum install yum-utils
    # yumdownloader --source <package>

Unpack rpm or src rpm: ::

    # rpm2cpio <rpm file> | cpio -idmv

List repo id and name of all repositories: ::

    # dnf repolist 

List all packages of a specified repository: ::

    # dnf repository-packages <repo id> list

Debuginfo
---------

::

    # dnf debuginfo-install <package>

    Or

    # dnf install <package>-debuginfo

https://fedoraproject.org/wiki/Packaging:Debuginfo


If you see an unfamiliar macro, you can evaluate it with: ::

    $ rpm --eval %{<macro>}

    e.g.
    $ rpm --eval %{_bindir}
    /usr/bin
    $ rpm --eval %{_libexecdir}
    /usr/libexec


::

    $ rpmdev-setuptree
    $ cd rpmbuild/SPECS
    $ rpmdev-newspec <pacakge>
    $ vim <package>.spec
    # Install dependences
    $ yum-builddep <package>.spec

References
----------

https://docs.fedoraproject.org/en-US/packaging-guidelines/

http://ftp.rpm.org/max-rpm/index.html
