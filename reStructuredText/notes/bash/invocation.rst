Bash invocaton
==============

login shell
    one whose first character of argument zero is a ``-``, or one started with
    the ``--login`` option.

interactive shell
    one started without non-option arguments (unless ``-s`` is specified) and
    without the -c option whose standard input and error are both connected to
    terminals (as determined by ``isatty``), or one started with the ``-i``
    option.

When bash is invoked as a login shell, it first reads and executes commands
from the file */etc/profile*, if that file  exists. After reading that file,
it looks for *~/.bash_profile*, *~/.bash_login*, and *~/.profile*, in that
order, and reads and executes commands from the first one that exists and is
readable.

When an interactive shell that is not a login shell is started, bash reads and
executes commands from *~/.bashrc*, if that file exists.

When bash is started non-interactively, to run a shell script, for example, it
looks for the variable ``BASH_ENV`` in the environment, expands its value if it
appears there, and  uses the expanded value as the name of a file to read and
execute.  Bash behaves as if the following command were executed: ::

    if [ -n "$BASH_ENV" ]; then . "$BASH_ENV"; fi

but the value of the PATH variable is not used to search for the filename.
