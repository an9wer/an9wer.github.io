Network
=======

Gateway
-------

`Wikipedia: Gateway <https://en.wikipedia.org/wiki/Gateway_%28telecommunications%29>`_
    A network gateway is used as protocol translators (e.g. Python WSGI)

    On an Internet Protocol (IP) network, IP packets with a destination outside
    a given subnet mask are send to the network gateway.

`Wikipedia: 0.0.0.0 <https://en.wikipedia.org/wiki/0.0.0.0>`_
    In the context of routing tables, a network destination of 0.0.0.0 is used
    with a network mask of 0 to depict the default route as a destination
    subnet.

    In routing tables, 0.0.0.0 can also appear in the gateway column. This
    generally means that no intermediate routing hops are necessary because the
    system is directly connected to the destination.

`Wikipedia: default route
<https://en.wikipedia.org/wiki/Default_route>`_

Broadcast
---------

MAC broadcast address: FF-FF-FF-FF-FF-FF

http://www.firewall.cx/networking-topics/general-networking/109-network-broadcast.html

`Wikipedia: Bootstrap Protocol
<https://en.wikipedia.org/wiki/Bootstrap_Protocol>`_

P344

IP broadcast address: 255.255.255.255
    When a host sends a datagram with broadcast address, the message is
    delivered to all hosts on the same subnet.


Link Layer
----------

Ethernet uses frame.


P445
A point-to-point link (e.g. PPP, HDLC) consists of a single sendr at one end of
the link and a single receiver at the other end of the link. A broadcast link
(e.g. Etherne, wireless LAN), on the other hand, has multiple sending and
receiving nodes all connected to the same, single, shared broadcast channel.

``man 7 arp``

ARP resolves IP addresses only for hosts and router interfaces on the same
subnet.

Each host and router has an ARP table in its memory, which contains mappings of
IP addresses to MAC address.

The ARP table contains a time-to-live (TTL) value, which indicates when each
mapping will be deleted from the table.

P468
To see send a network-layer datagram to another subnet across a router.

For each router interface there is also an ARP module (in the router) and an
adapter.

LAN technologies:

-   Ethernet
-   FDDI
-   ATM

Ethernet has been to local area networking what the internet has been to global
networking.

CRC (Cycli redundance check)

Ethernet CDMA/CD protocol
    https://www.geeksforgeeks.org/collision-detection-csmacd/

P476
Switch itself is transparent to the hosts and routers in the subnet; that is, a
host/router addresses a frame to another host/router (rather than addressing
the frame to the switch) and happily sends the frame into the LAN, unaware that
a switch will be receiving the frame and forwarding it.

**Filtering** is the switch function that determines whether a frame should be
forwarded to some interface or should just be dropped.

**Forwarding** is the switch function that determines the interfaces to which a
frame should be directed, and then moves the frame to those interfaces.

Switch filtering and forwarding are done with a **switch table**.

Switch table contains (but not necessarily all):
1.  MAC address
2.  Switch interface that leads toward that MAC
3.  Time at which the entry was placed in the table

P477
Understand how siwthc filtering and forwarding work:

-   There is no entry in the table for 'DD-DD-DD-DD-DD-DD-DD'. In this case,
    the switch forwards copies of the frame to the output buffers preceding all
    interfaces except for the sender interface itself.
-   There is an entry in the table for 'DD-DD-DD-DD-DD-DD-DD' with the
    interface same as the sender interface itself, the switch performs the
    filtering function by discarding the frame.
-   There is an entry in the table, associating 'DD-DD-DD-DD-DD-DD-DD' with
    another interface different from the sender interface, the switch performs
    its forwarding fuction by putting the frame in an output buffer that
    precedes to target interface.


P478

Switches self-learn
    For each incoming frame received on an interfacce, the switch stores in its
    table :

        1.  MAC address in the frame's source address field.
        2.  Interface from which frame arrived
        3.  Current time

P479
Switches are also full-duplex, meaning any switch interface can send and
receive at the same time.

P480
Switch sniff

Network Layer
-------------

Internet Protocol (IP) uses datagram.

Host-to-host commmunication

Network layer protocol:

-   IP
-   IPX
-   AppleTalk

P313
Computer networks that provide only a connection service at the network layer
are called virtual-circuit (VC) networks (e.g. IP); computer networks that
provide only a connectionless service at the network layer are called datagram
networks (e.g.  ATM, frame relay).

IP (Internet Protocol)
    A best-effort delivery service, which means that IP makes its "best effort"
    to deliver segments between communication hosts, but it makes no
    guarantees. (P190)

MTU
    In computer networking, the maximum transmission unit (MTU) is the size of
    the largest protocol data unit (PDU) that can be communicated in a single
    network layer transaction. The MTU relates to, but is not identical to the
    maximum frame size that can be transported on the data link layer, e.g.
    Ethernet frame.

    Larger MTU is associated with reduced overhead. Smaller MTU values can
    reduce network delay. 

    https://en.wikipedia.org/wiki/Maximum_transmission_unit

P318
When there are multiple matches, the router uses the **longest prefix
matching** rule; that is, it finds the longest matching entry in the table and
forwards the packet to the link interface associated with the longest prefix
match.

P321
If there are a 10 Gbps input link and a 64-byte IP datagram, the input port has
only 51.2 ns to process the datagram berfore anotehr datagram may arrive. ::

    1 / ( 10 * 1000 / 8 / 64)

P335
IP Datagram Fragmentation

P344

Classful addressing
    Use 8-, 16-, 24-bit subnet address, which are known as class A, B, and C
    networks, respectively.

Classless Interdomain Routing (CIDR)
    `Wikipedia: CIDR
    <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_

P346

DHCP
    A plug-and play protocol

    Address lease time is the amount of time for which the IP address will be
    valid.

    Use 255.255.255.255 as destination address to broadcast to all hosts in
    subnet.

P353
ICMP is often considered part of IP but architecturally it lies just above IP,
as ICMP messages are carried inside IP datagram.

The well-known ping program sends an ICMP type 8 code and 0 message to the
specified host. The destination host, seeing the echo request, sends back a
type 0 code 0 ICMP echo reply.

`Wikipedia: ICMP
<https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol>`_

`RFC 792: ICMP
<https://tools.ietf.org/html/rfc792>`_

NAT
https://www.slashroot.in/linux-nat-network-address-translation-router-explained

https://serverfault.com/a/119374


Round-trip time
    `Wikipedia: RTT
    <https://en.wikipedia.org/wiki/Round-trip_delay_time>`_

RIP, OSPF, BGP
    http://sabercomlogica.com/en/ebook/intra-as-and-inter-as-routing/
    

Source routing
     Route packets using their source addresses.

    `Wikipedia: source routing
    <https://en.wikipedia.org/wiki/Source_routing>`_

Policy-based routing
     Route packets using their source addresses.

    `Wikipedia: policy-based routing
    <https://en.wikipedia.org/wiki/Policy-based_routing>`_

`Source routing vs policy-based routing
<https://learningnetwork.cisco.com/thread/86495>`_


Transport Layer
---------------

Segment

Process-to-process communication
 

TCP
---

Connection provided by the TCP/IP are full duplex. it consists of two
independent streams flowing in opposite directions, with no apparent
interaction. The stream service allows an application process to terminate flow
in on direction while data continues to flow in the other direction , making
the connection half duplex.

Positive acknowledgement with retransmission

Segment

Error detection
    checksum

Receiver feedback
    ACK

Retransmission


References
----------

`Wikipedia: TCP
<https://en.wikipedia.org/wiki/Transmission_Control_Protocol>`_

`How does internet work
<https://howdoesinternetwork.com/>`_
