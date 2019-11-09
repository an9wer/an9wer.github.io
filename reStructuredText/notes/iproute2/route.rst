Iproute2 route
==============

::

    ip route { add | del | change | append | replace } ROUTE

    ROUTE := NODE_SPEC [ INFO_SPEC ]

    NODE_SPEC := [ TYPE ] PREFIX [ tos TOS ] [ table TABLE_ID ] [ proto RTPROTO]
      [ scope SCOPE ] [ metric METRIC ] [ ttl-propagate { enabled | disabled } ]

    INFO_SPEC := { NH | nhid ID } OPTIONS FLAGS [ nexthop NH ] ...

**Note**: the braces indicate a choice list, and the fields in brackets are
optional.
