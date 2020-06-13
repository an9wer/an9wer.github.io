Systemd tmpfile
===============

systemd-tmpfiles creates, deletes, and cleans up volatile and temporary files
and directories, based on the configuration file format and location specified
in tmpfiles.d.

System services (systemd-tmpfiles-setup.service,
systemd-tmpfiles-setup-dev.service, systemd-tmpfiles-clean.service) invoke
systemd-tmpfiles to create system files and to perform system wide cleanup.


References
----------

``man systemd-tmpfiles``

``man tmpfiles.d``
