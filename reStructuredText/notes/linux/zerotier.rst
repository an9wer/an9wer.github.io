Linux Zerotier
==============

Install zerotier-one: ::

    # curl -s https://install.zerotier.com | bash
    # systemctl start zerotier-one.service

Join network: ::

    # zerotier-cli join <network id>

Create moon
-----------

Server: ::

    # cd /var/lib/zerotier-one
    # zerotier-idtool initmoon identity.public > moon.json
    # vim moon.json
        "stableEndpoints": [ "<public ip>/9993" ]
    # mkdir moons.d
    # cd moons.d
    # zerotier-idtool genmoon ../moon.json
    # systemctl restart zerotier-one

Client: ::

    # zerotier-cli orbit <world id> <seed>
    
    or

    Download '/var/lib/zerotier-one/moons.d/xxx.moon' file from server to
    '/var/lib/zerotier-one/moons.d/' directory at client side and then run
    `systemctl restart zerotier-one.service`


References
----------

`zerotier内网穿透以及moon节点配置
<https://imgki.com/archives/234.html>`_
