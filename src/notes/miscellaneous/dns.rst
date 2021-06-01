.. meta::
    :robots: noindex

DNS
===

**Note**: DNS can use both UDP and TCP port to make request and response. DNS
primarily uses the UDP on port number 53 to serve requests. DNS queries consist
of a single UDP request from the client followed by a single UDP reply from the
server. When the length of the answer exceeds 512 bytes and both client and
server support EDNS, larger UDP packets are used. Otherwise, the query is sent
again using the TCP. TCP is also used for tasks such as zone transfers. Some
resolver implementations use TCP for all queries. 

TTL
---

TODO

EDNS
----

EDNS is essential for the implementation of DNS Security Extensions (DNSSEC).
EDNS is also used for sending general information from resolvers to name
servers about clients' geographic location in the form of the EDNS *Client
Subnet (ECS)* option. ::

    $ dig @223.5.5.5 +tcp google.com
    $ dig @223.5.5.5 +tcp google.com +subnet=127.0.0.1

References
----------

`Wikipedia: DNS
<https://en.wikipedia.org/wiki/Domain_Name_System>`_

`Wikipedia: EDNS
<https://en.wikipedia.org/wiki/Extension_mechanisms_for_DNS>`_
