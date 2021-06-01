.. meta::
    :robots: noindex

Systemd journal
===============

The journal service stores log data either persistently below
*/var/log/journal* or in a volatile way below */run/log/journal/* (in the
latter case it is lost at reboot). By default, log data is stored persistently
if /var/log/journal/ exists during boot, with an implicit fallback to volatile
storage otherwise.  Use ``Storage=`` in journald.conf to configure where log
data is placed, independently of the existence of */var/log/journal/*.

On systems where /var/log/journal/ does not exist yet but where persistent
logging is desired (and the default journald.conf is used), it is sufficient to
create the directory, and ensure it has the correct access modes and ownership:
::

    # mkdir -p /var/log/journal
    # systemd-tmpfiles --create --prefix /var/log/journal
    # systemctl restart systemd-journald


References
----------

``man systemd-journald``

``man journald.conf``
