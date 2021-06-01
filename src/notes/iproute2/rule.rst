.. meta::
    :robots: noindex

Iproute2 rule
=============

Each policy routing rule consists of a *selector* and an *action predicate*.

The *selector* of each rule is applied to *source address*, *destination
address*, *incoming interface*, *tos*, *fwmark* and, if the selector matches
the packet, the *action* is performed.

::

    ip rule "add|del" <SELECTOR> <ACTION>

    SELECTOR := [not] [from <PREFIX>] [to <PREFIX> ] [tos <TOS>] [fwmark <FWMARK>[/<MASK>] ]
        [iif <STRING>] [oif <STRING>] [pref <NUMBER>] [l3mdev ] [uidrange <NUMBER-NUMBER>]
        [ipproto <PROTOCOL>] [sport [<NUMBER>|<NUMBER-NUMBER>]]
        [dport [<NUMBER>|<NUMBER-NUMBER>]] [tun_id <TUN_ID>]

    ACTION := [table <TABLE_ID>] [protocol <PROTO>] [nat <ADDRESS>]
        [realms [<SRCREALM>/]<DSTREALM>] [goto <NUMBER>] <SUPPRESSOR>

ACTION
------

table
    The routing table identifier to lookup if the rule selector matches: ::

        # ip rule add fwmark 1 table 100

    It is also possible to use lookup instead of table: ::

        # ip rule add fwmark 1 lookup 100



References
----------

``man ip-rule``
