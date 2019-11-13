SSH
===

-A
    Enables forwarding of the authentication agent connection.

    ::

        $ eval ssh-agent $SHELL
        $ ssh-add ~/.ssh/<destinationAB's private key>
        $ # From host
        $ ssh -A <destinationA>
        $ # From destinationA
        $ ssh <destinationB>

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
    other interface set by *bind_address*).

An empty *bind_address* indicates that it will listen to loopback interface
(127.0.0.1), the address \* means that it will listen to all interface
(0.0.0.0). Specifying a *bind_address* will only succeed if the server's
*GatewayPorts* option is enabled.

Use ``-fN`` option to make ssh port forwarding run at background: ::

    ssh -fN -L|-R [bind_address:]port:host:hostport destination

SSH tunnel references
"""""""""""""""""""""

`Stackoverflow: ssh forwarding
<https://unix.stackexchange.com/a/115906>`_


SSHD config
-----------

See ``man sshd_config``

GatewayPorts
    Specify that sshd should allow remote port forwardings to bind to
    non-loopback addresses, thus allowing other hosts to connect.

    The argument may be *no* to force remote port forwardings to be available
    to the local host only, *yes* to force remote port forwardings to bind to
    the wildcard address.

ssh-keygen
----------

Generate the missing public key again from the private key: ::

    $ ssh-keygen -y -f <private key>

Display fingerprint of public key: ::

    $ ssh-keygen -l -f <private key or publick key>


authorized_keys
---------------

See ``man sshd``

Each line of the file contains one key (empty lines and lines starting with a
"#" are ignored as comments). Public keys consist of the following
space-separated fields: ::

    [<options>] <keytype> <base64-encoded key> <comment>

The keytype is “ecdsa-sha2-nistp256”, "ecdsa-sha2-nistp384",
"ecdsa-sha2-nistp521", "ssh-ed25519", "ssh-dss" or "ssh-rsa";

the comment field is not used for anything (but may be convenient for the user
to identify the key).
