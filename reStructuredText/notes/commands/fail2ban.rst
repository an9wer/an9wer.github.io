.. meta::
    :robots: noindex

Fail2ban
========

Check status of all jails: ::

    # fail2ban-client status

Check status of specified jail: ::

    # fail2ban-client status <jail>

List all actions of specified jail: ::

    # fail2ban-client get <jail> actions

Get specified action of jail: ::

    # fail2ban-client get <jail> action <action> "actionstart|actionstop|actioncheck|actionban|actionunban|timeout"

Get action properties of jail: ::

    # fail2ban-client get <jail> actionproperties <action>

Unban ip address: ::

    # fail2ban-client set <jail> unbanip <ip>

References
----------

``man fail2ban-client``

``man jail.conf``
