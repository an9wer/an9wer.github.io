lsof
====

Command syntax: ::

    lsof [options] [--] [[name] ...]

----

To find the process that has the specified file open: ::

    # lsof <file>

To list all open files on the mounted-on directory (e.g. /, /mnt): ::

    # lsof <mounted-on directory>

To list all open files on device (e.g. /dev/sda): ::

    # lsof <device>

Scan directory (not descend the directory tree): ::

    # lsof +d <directory>

Scan directory, follow symbolic links and/or filesystems: ::

    # lsof +d <directory> "-x|-x l|-x f"

Scan directory tree (include all subdirectories): ::

    # lsof +D <directory>

Scan directory tree, follow symbolic links and/or filesystems: ::

    # lsof +D <directory> "-x|-x l|-x f"

Show all open socket file: ::

    # lsof -i [46][protocol][@hostname|@hostaddr][:service|:port]

Show open socket file in specified state: ::

    # lsof -i [46][TCP|UDP][@hostname|@hostaddr][:service|:port] -s TCP|UDP:ESTABLISHED|LISTEN

List files for specified processes: ::

    # lsof -p <pid>[,<pid>...]
    
List all UNIX domain socket files: ::

    # lsof -U

List UNIX domain socket files for specified processes (use ``-a`` option, see
`OR AND`_): ::

    # lsof -U -a -p <pid>[,<pid>...]

Select the fields to be output (use ``lsof -F?`` to list all support
characters): ::

    # lsof -F <char>[<char>..]
    

.. _OR AND:

- OR AND:

  Normal list options of ``lsof`` are ORed (i.e. specifying the ``-i`` option
  without an address and the ``-ufoo`` option produces a listiong of all
  network files OR files belonging to processes owned by user 'foo'). The
  exceptions are:

  1. the ``^`` (negated) login name or user ID (UID), specified with the ``-u``
     option.

  2. the ``^`` (negated) process ID (PID), specified with the ``-p`` option.

  3. the  ``^`` (negated) process group ID (PGID), specified with the ``-g``
     option.

  4. the ``^`` (negated) command, specified with the ``-c`` option;

  5. the ``^`` (negated) TCP or UDP protocol state names, specified with the
     ``-s [p:s]`` option.

  The ``-a`` option may be used to AND the selections.

References
----------

``man lsof``
