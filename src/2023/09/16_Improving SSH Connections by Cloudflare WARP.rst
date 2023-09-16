Improving SSH Connections by Cloudflare WARP
============================================

:Published: 2023/09/16

.. meta::
    :description: Using Clodflare WARP to decrease network latency and  improve
            the quality of SSH connection to my remote server.

The quality of a SSH connection to a remote server is always poor when the
remote server is truely remote - so far away from me. As network packets of a
SSH connection, heading to the remote server, have to go through a series of
routing hops, the further the distance usually means the higher the network
latency. Moreover, The situation gets worse when the network connection is not
stable, in which a few parts of the packets are lost on their way to reach the
remote server.

The experience of performing operation on my remote server via SSH is highly
connected to the network latency. A bad experience is when typing commands,
moving the cursor between words, or scrolling the screen of a man page, I can
apparently notice the delay between my input and the reaction from my remote
server.

The simplest solution is buying a new server that is close to me, but it is
not practical obviously. Another possible solution is with the help of another
server in the middle, which should have lower network latency for both sides,
but I still have to buy a new server to work as the middle server.

Finally, I found a free solution - Cloudflare WARP, which is based on Wireguard
protocol and provides a way of making the connection faster [#]_. Cloudflare
WARP can transfer my original SSH connections to Cloudflare's own global
network to promise lower network latency and packet loss. ::

    .----.     .-----------------.      .---------------------------.     .------------------.
    | me | --> | Cloudflare edge |  --> |      Cloudflare edge      | --> | my remote server |
    `----'     |   close to me   |      | close to my remote server |     `------------------'
               `-----------------'      `---------------------------'

Instructions of using Cloudflare WARP for SSH connections
---------------------------------------------------------

Running a WARP sevice: ::

    $ warp-svc    # set cap before use

Initializing WARP connection in the socks5 proxy mode, by default listening on
``127.0.0.1:40000``: ::

    $ warp-cli register
    $ warp-cli set-mode proxy
    $ warp-cli connect

Forwarding SSH connections to WARP's socks5 proxy: ::

    $ nano ~/.ssh/config
        Host my-remote-server
            ProxyCommand nc -X 5 -x 127.0.0.1:40000 %h %p

The last issue I detected is that SSH connections will be closed suddenly if no
actions in the next 10 seconds. I guess that was WARP's default rule of closing
any inactive sessions. Thus, to keep SSH connections alive I have to add the
below settings: ::

    $ nano ~/.ssh/config
        Host my-remote-server
            ServerAliveInterval 5   # less than 10 seconds
            ServerAliveCountMax 12

Thanks for reading :)


References
----------

.. [#] `Cloudflare: Introducing WARP <https://blog.cloudflare.com/1111-warp-better-vpn/>`_
