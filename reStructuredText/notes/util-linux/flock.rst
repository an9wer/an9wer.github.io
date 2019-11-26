Util-linux flock
================

Command syntax: ::

    flock [options] <file> <command> [<argument> ...]

Obtain an exclusive lock (which is a default behavior): ::

    $ flock "-e|-x" <file> <command> [<argument> ...]

    Example:
    shell1> $ flock /tmp/lockfile sleep 30
    shell2> $ flock -n /tmp/lockfile echo gotcha

Obtain a shared lock: ::

    # flock -s <file> <command> [<argument> ...]

    Example:
    shell1> $ flock -s /tmp/lockfile sleep 30
    shell2> $ flock -s -n /tmp/lockfile echo gotcha
