Collectd
========

Parse rrd to generate graphics and html in current directory: ::

    $ perl /usr/share/collectd/collectd2html.pl

List all values available to the "unixsock" plugin: ::

    $  collectdctl -s <unixsock> listval
