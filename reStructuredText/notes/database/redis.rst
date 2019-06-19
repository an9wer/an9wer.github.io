Redis
=====

Redis replication
-----------------

Redis replication allows slave instances to be exact copies of master
instances. When some errors happen, master will be replaced by one of slaves.

Setup redis replication
"""""""""""""""""""""""

To configure basic Redis replication, just add the following line to the slave
configuration file:

::

    slaveof <ip/hostname> <port>

Or run the following line in redis client interface of slave (this means we can
set redis server to be a slave even when it is running):

::

    > SLAVEOF <ip/hostname> <port>

By default, slaves are read-only, which means you cannot modify any data of
slaves by using *redis-cli*, but only master of slaves can, this behavior is
controlled by the *slave-read-only* only option in the *redis.conf* file, 
    
Turn off redis replication
""""""""""""""""""""""""""

To turn off redis replication or turn the slave into a master:

::

    > SLAVEOF NO ONE 

Set slave to authenticate to a master
"""""""""""""""""""""""""""""""""""""

If master instance have a password via *reqirepass*:

::

    > CONFIG SET requirepass <password>

To synchronous data from master, slaves need to authenticate first:

::

    > CONFIG SET masterauth <password>

References
""""""""""

-   `Redis official documentation: replication <https://redis.io/topics/replication>`_

