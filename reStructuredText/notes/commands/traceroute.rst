Traceroute
==========

Set the number of probe packets per hop (by default is 3): ::

    # traceroute -q <number> <destionation>

Use ICMP method for probes: ::

    # traceroute "-I|--icmp" <destionation>

Use TCP SYN for probes: ::

    # traceroute "-T|--tcp" <destionation>


Methods
=======

In the modern network environment the traditional traceroute methods can not be
always applicable, because of widespread use of firewalls. Such firewalls
filter the "unlikely" UDP ports, or even ICMP echoes. To solve this, some
additional tracerouting methods are implemented (including tcp). Such methods
try to use particular protocol and source/destination port, in order to bypass
firewalls.

Default
     Probe packets are udp datagrams with so-called "unlikely" destination
     ports.

     The "unlikely" port of the first probe is 33434, then for each next probe
     it is incremented by  one.  Since the ports are expected to be unused,
     the destination host normally returns "icmp unreach port" as a final
     response. (Nobody knows what happens when some application listens for
     such ports, though).

