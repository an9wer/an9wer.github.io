SSH
===

SSH tunnel
----------

::

    ssh -L [bind_address:]port:host:hostport destination
    ssh -R [bind_address:]port:host:hostport destination

In these commands, *destination* is like a bridge, it connects between local
and remote side:

-   -L: *port* is loacted at local side, *host* and *hostport* is used at
    remote side. The tunnel forwards remote *host:hostport* to local *port*,
    then we can visit remocal service locally through *127.0.0.1:port* (or
    other interface set by *bind_address*).

-   -R: *port* is located at remote side. *host* and *hostport* is used at
    loacl side. The tunnel forwards local *host:hostport* to remote *port*,
    then remote host can visit local side service through *127.0.0.1:port* (or
    other interface set bhy *bind_address*).

An empty *bind_address* indicates that it will listen to loopback interface
(127.0.0.1), the address \* means that it will listen to all interface
(0.0.0.0). Specifying a *bind_address* will only succeed if the server's
*GatewayPorts* option is enabled.

References
    https://unix.stackexchange.com/a/115906


SSHD config
-----------

See ``man sshd_config``

GatewayPorts
    Specify that sshd should allow remote port forwardings to bind to
    non-loopback addresses, thus allowing other hosts to connect.

    The argument may be *no* to force remote port forwardings to be available
    to the local host only, *yes* to force remote port forwardings to bind to
    the wildcard address.

kill -9 

ps -efw

mv /opt/microsoft/servicefabric{,.bak}
mv /mnt/sfroot{,.bak}
