Linux wireguard
===============

Generate private key: ::

    # wg genkey

Case 1
------

A and B are servers with public IP. To peer A and B.

Configuration of A: ::

    [Interface]
    Address = 192.168.2.1/24
    ListenPort = <listen port of A>
    PrivateKey = <private key of A>

    [Peer]
    PublicKey = <public key of B>
    AllowedIPs = 192.168.2.2/32

Configuration of B: ::

    [Interface]
    Address = 192.168.2.2/24
    ListenPort = <listen port of B>
    PrivateKey = <private key of B>

    [Peer]
    Endpoint = <public ip of A>:<port of A>
    PublicKey = <public key of A>
    AllowedIPs = 192.168.2.1/32

Then, ``ping`` from B to A and reverse are ok.

Case 2
------

A is a server with public IP and B is a local machine behind a NAT router. To 
peer A and B.

Configuration of A: ::

    [Interface]
    Address = 192.168.2.1/24
    ListenPort = <listen port of A>
    PrivateKey = <private key of A>

    [Peer]
    PublicKey = <public key of B>
    AllowedIPs = 192.168.2.2/32

Configuration of B: ::

    [Interface]
    Address = 192.168.2.2/24
    ListenPort = <listen port of B>
    PrivateKey = <private key of B>

    [Peer]
    Endpoint = <public ip of A>:<port of A>
    PublicKey = <public key of A>
    AllowedIPs = 192.168.2.1/32
    PersistentKeepalive = 25

Then, ``ping`` from B to A and reverse are ok.

Case 3
------

A is a server with public IP and B is a local machine behind a NAT router. To 
forward all traffic of B through A.

Configuration of A: ::

    # sysctl -w net.ipv4.ip_forward=1

    [Interface]
    Address = 192.168.2.1/24
    ListenPort = <listen port of A>
    PrivateKey = <private key of A>
    PostUp = iptables -t nat -i <interface of A's wireguard> -A POSTROUTING -j MASQUERADE
    PostDown = iptables -t nat -i <interface of A's wireguard> -D POSTROUTING -j MASQUERADE

    [Peer]
    PublicKey = <public key of B>
    AllowedIPs = 192.168.2.2/32
    
Configuration of B: ::

    [Interface]
    PrivateKey = <private key of B>
    Address = 192.168.2.2/24

    [Peer]
    PublicKey = <public key of A>
    Endpoint = <IP of A>:<port of A>
    AllowedIPs = 0.0.0.0/0
    PersistentKeepalive = 25

Then, ``curl ifconfig.me`` from B gets A's public IP.

Case 4
------

A is a server with public IP and B, C are local machines behind NAT router. To 
peer B and C.

Configuration of A: ::

    [Interface]
    Address = 192.168.2.1/24
    ListenPort = <listen port of A>
    PrivateKey = <private key of A>

    [Peer]
    PublicKey = <public key of B>
    AllowedIPs = 192.168.2.2/32

    [Peer]
    PublicKey = <public key of C>
    AllowedIPs = 192.168.2.3/32

Configuration of B: ::

    [Interface]
    PrivateKey = <private key of B>
    Address = 192.168.2.2/24

    [Peer]
    PublicKey = <public key of A>
    Endpoint = <IP of A>:<port of A>
    AllowedIPs = 192.168.2.0/24
    PersistentKeepalive = 25

Configuration of C: ::

    [Interface]
    PrivateKey = <private key of B>
    Address = 192.168.2.3/24

    [Peer]
    PublicKey = <public key of A>
    Endpoint = <IP of A>:<port of A>
    AllowedIPs = 192.168.2.0/24
    PersistentKeepalive = 25

Then, ``ping`` from B to C and reverse are ok.

Case 5
------

A is a server with public IP and B, C are local machines behind NAT router. To 
forward all traffic of B through C.

Configuration of A: ::

    # sysctl -w net.ipv4.ip_forward=1

    [Interface]
    Address = 192.168.2.1/24
    ListenPort = <listen port of A>
    PrivateKey = <private key of A>
    PostUp = iptables -t nat -i <interface of A's wireguard> -A POSTROUTING -j MASQUERADE
    PostDown = iptables -t nat -i <interface of A's wireguard> -D POSTROUTING -j MASQUERADE

    [Peer]
    PublicKey = <public key of B>
    AllowedIPs = 192.168.2.2/32

    [Peer]
    PublicKey = <public key of C>
    AllowedIPs = 0.0.0.0/0
    
Configuration of B: ::

    [Interface]
    PrivateKey = <private key of B>
    Address = 192.168.2.2/24

    [Peer]
    PublicKey = <public key of A>
    Endpoint = <IP of A>:<port of A>
    AllowedIPs = 0.0.0.0/0
    PersistentKeepalive = 25

Configuration of C: ::

    # sysctl -w net.ipv4.ip_forward=1

    [Interface]
    PrivateKey = <private key of C>
    Address = 192.168.2.3/24
    PostUp = iptables -t nat -i <public interface of C> -A POSTROUTING -j MASQUERADE
    PostDown = iptables -t nat -i <public interface of C> -D POSTROUTING -j MASQUERADE

    [Peer]
    PublicKey = <public key of A>
    Endpoint = <IP of A>:<port of A>
    AllowedIPs = 192.168.2.1/32
    PersistentKeepalive = 25

Then, ``curl ifconfig.me`` from B gets C's public IP.
