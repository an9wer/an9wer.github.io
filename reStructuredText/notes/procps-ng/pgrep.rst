Procps-ng pgrep
===============

``pgrep`` and ``pkill`` use the same options (the exceptions are ``-l`` and
``-a`` which can only be used by ``pgrep``).

List the process name as well as the process id: ::

    $ pgrep -l <pattern>

List hte full command line as well as the process id: ::

    $ pgrep -a <pattern>
    
Ignore case when matching processes: ::

    $ pgrep -i <pattern>

Set another string (by default a newline) to delimit process id: ::

    $ pgrep -d <delimiter> <pattern>
