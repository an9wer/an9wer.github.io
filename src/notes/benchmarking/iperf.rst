.. meta::
    :robots: noindex

Iperf
=====

Iperf2
------

Start up a server and bind to specific interface: ::

    $ iperf -s [-B <interface>]


Start up a client and bind to specific interface (if needed):: ::

    $ iperf -c <destination> [-B <interface>]

Start up a client in dualtest mode, which running reverse test simultaneously: ::

    $ iperf -c <destination> -d [-L <port>]

Start up a client in tradeoff mode, which runing reverse test individually: ::

    $ iperf -c <destination> -r [-L <port>]

-   Reverse test will cause the server to connect back to the client on the
    port specified in the *-L* option (or defaults to the port the client
    connected to the server on).

Set the client running time in second, default is 10: ::

    $ iperf -c <destination> -t <time>



Iperf3
------

Start up a server and bind to specific interface: ::

    $ iperf3 -s [-B <interface>]


Start up a client and bind to specific interface (if needed): ::

    $ iperf3 -c <destination> [-B <interface>]

Start up client in reverse mode (server sends data to client): ::

    $ iperf3 -c <destination> -R

Set the client running time in seconds, default is 10: ::

    $ iperf3 -c <destination> -t <time>

Set interval time in seconds between periodic, default is 1, use 0 to disable: ::

    $ iperf3 -c <destination> -i <time>

-   The 'Retr' field in output is the number of TCP segments retransmitted.
    This can happen if TCP segments are lost in the network due to congestion
    or corruption.  (see `here <https://github.com/esnet/iperf/issues/343>`_)
