.. meta::
    :robots: noindex

Iproute2 route
==============

::

    ip route "add|del|change|append|replace" <ROUTE>

    ROUTE := <NODE_SPEC> [<INFO_SPEC>]

    NODE_SPEC := [<TYPE>] <PREFIX> [tos <TOS>] [table <TABLE_ID>] [proto <RTPROTO>]
      [scope <SCOPE>] [metric <METRIC>] [ttl-propagate "enabled|disabled"]

    INFO_SPEC := "NH|nhid ID" <OPTIONS> <FLAGS> [nexthop <NH>] ...

Add route to table: ::

    # ip route add <prefix> table <table>

**Note**: When prefix value is ``default``, it means ``0.0.0.0/0``, so the
following two statements are equal: ::

    # ip route add default via 192.168.0.1

    # ip route add 0.0.0.0/0 via 192.168.0.1

References
----------

``man ip-route``
