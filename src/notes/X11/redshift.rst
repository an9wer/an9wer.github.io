.. meta::
    :robots: noindex

Redshift
========

By default redshift will use *geoclue2* to get location information, but in my
case, it stucks at `Waiting for initial location to become available...` when
running without any arguments.

So manually set my location and daytime and night tempurature: ::

    $ redshift -l <LATITUDE:LONGTITUDE> -t <DAY:NIGHT>

To only print (not run) parameter the redshif will execute: ::

    $ redshift -l <LATITUDE:LONGTITUDE> -t <DAY:NIGHT> -p

To instantly adjusts the color temperature: ::

    $ redshift -P -O <TEMPERATURE>
    
To reset all: ::

    $ redshift -x
    
Update 2020/10/14
-----------------

Fortunately, now *geoclue2* works well with redshift on my new gentoo system: ::

    $ redshift -l geoclue2 -t <DAY:NIGHT>

References
----------

`Official website
<http://jonls.dk/redshift/>`_

`Archwiki: redshift
<https://wiki.archlinux.org/index.php/Redshift>`_
