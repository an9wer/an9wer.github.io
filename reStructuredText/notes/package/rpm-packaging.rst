Package rpm-packaging
=====================

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
    $ yum-builddep <package>.spec
