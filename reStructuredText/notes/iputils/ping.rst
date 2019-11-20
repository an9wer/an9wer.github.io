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

Flood ping: ::

    # ping -f <destionation>

Set interval senconds between sending each packet. The default is to wait for
on second between each packet normally, or not to wait in flood mode. Only
super-user may set interval to values less than 0.2 seconds: ::

    $ ping -i <interval> <destionation>


References
----------

``man ping``
