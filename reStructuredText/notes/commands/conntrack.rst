Conntrack
=========

conntrack is command line interface conntrack provides a more flexible
interface to the connnection tracking system than ``/proc/net/ip_conntrack``
(In morden linux is ``/proc/net/nf_conntrack``).  With conntrack, you can show,
delete and update the existing state entries; and you can also listen to flow
events.

conntrackd is the user-space connection tracking daemon. This daemon can be
used to deploy fault-tolerant GNU/Linux firewalls but you can also use it to
collect flow-based statistics of the firewall use.
