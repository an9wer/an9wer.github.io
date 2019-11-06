Ping
====

Stop after sending count ECHO_REQUEST packets: ::

    $ ping -c <count> <destionation>

Stop when deadline expire: ::

    $ ping -w <time> <destionation>

Quite mode, only display the summary lines: ::

    $ ping -q <destionation>

Set TTL (time to live) for every queries: ::

    $ ping -t <ttl> <destionation>
