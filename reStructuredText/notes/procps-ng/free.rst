Procps-ng free
==============

The information of ``free`` is gathered by parsing */proc/meminfo*.


Display in mebibytes: ::

    $ free -m

Display in megabytes: ::

    $ free -m --si


Continuously display the result: ::

    $ free -s <interval>

Continuously display the result in certain times: ::

    $ free -s <interval> -c <times>

Report buffers and cache in two separate columns: ::

    $ free -w
