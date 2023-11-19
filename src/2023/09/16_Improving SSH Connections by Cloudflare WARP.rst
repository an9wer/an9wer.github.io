Improving SSH Connections by Cloudflare WARP
============================================

:Published: 2023/09/16

.. meta::
	:tags: network
	:description: Using Clodflare WARP to decrease network latency and
		improve the quality of SSH connection to my remote server.

Usually, a poor SSH connection to a remote server happens when the remote
server is truely "remote" - locating far away from your position, as network
packets have to go through more routing hops to reach out the remote server,
leading to a high network latency, and perhaps a high packet loss ratio.

Why does it matter? If the quality of a SSH connection is terriable, you can
apparently feel the delay between your input and the reaction from the remote
server, while performing operations on a remote server, such as typing commands,
moving cursors, or scrolling screens.

How to solve that? One solution is to set up another server which resides
between the remote server and you. The only requirement it should meet is to
provide a stable and low-latency network to both sides. However, it is not
easy to find such a server, or if you are luck to find one, you still need to
pay for it.

So, here is Cloudflare WARP, a free VPN service [#]_. Although its goal of
design is to secure Internet, you can also take advantage of its stable and
low-latency network to speed up your SSH connections. ::

	.-----.     .-----------------.      .----------------------------.     .-------------------.
	| you | --> | Cloudflare edge |  --> |      Cloudflare edge       | --> | the remote server |
	`-----'     |  close to you   |      | close to the remote server |     `-------------------'
	            `-----------------'      `----------------------------'

To use Cloudflare WARP, download its package from `its website`_, and here are
the instructions of using it for SSH connections on Linux.

Instructions of using Cloudflare WARP for SSH connections
---------------------------------------------------------

Start a Couldflare WARP client service locally: ::

	$ warp-svc

Set the Cloudflare WARP client to run as a socks5 proxy, listening on
``127.0.0.1:40000``: ::

	$ warp-cli set-mode proxy

Connect the Cloudflare WARP client to Cloudflare WARP's edge network: ::

	$ warp-cli register
	$ warp-cli connect

Forward SSH connections to Cludflare WARP's edge network through the socks5
proxy: ::

	$ nano ~/.ssh/config
		Host my-remote-server
			ProxyCommand nc -X 5 -x 127.0.0.1:40000 %h %p

Another issue I encountered was that SSH connections would be closed in a sudden
if I didn't continue to do any operations for the next few seconds (around 10s).
I suspect there is a rule set by Cloudflare WARP, which will close any inactive
sessions exceeding to a specific time. Thus, to keep SSH connections alive I
have to add the below settings to make ssh client send an alive message every
a few seconds, which must be lower than the time set by Cloudflare WARP to close
inactive sessions: ::

	$ nano ~/.ssh/config
		Host my-remote-server
			ServerAliveInterval 5
			ServerAliveCountMax 12

Thanks for reading :)

Further Readings
----------------

.. [#] `Cloudflare: Introducing WARP <https://blog.cloudflare.com/1111-warp-better-vpn/>`_


.. _its website: https://1.1.1.1/
