Iproute2 address
================

Syntax of ``ip address``: ::

    ip address "add|change|replace"
      <address>/<prefix> [broadcast <broadcast>] [label <label>] [scope <scope>]
      dev <interface> [valid_lft <lifetime>] [preferred_lft <lifetime>] [noprefixroute] [autojoin]

noprefixroute
    By default, when adding a new ip address to an interface, a router rule for
    the network prefix of that added address will also be created, but use
    ``noprefixroute`` will prevent this behavior, and don't search for one to
    delete when removing the address: ::

        # ip address add 172.16.0.7/16 dev eth0 noprefixroute
        
secondary
    When assigning more than one ip address to an interface and using the same
    prefix, the additional addresses are flagged secondary: ::

        # ip address add 172.16.0.7/16 dev eth0
        # ip address add 172.16.0.8/16 dev eth0
        # ip address add 172.16.0.9/16 dev eth0
