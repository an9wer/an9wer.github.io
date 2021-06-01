.. meta::
    :robots: noindex

Bash Grammar
============

Simple commands
---------------

A simple command is a sequence of optional variable assignments followed by
blank-separated words and redirections, and terminated by a control operator.
The first word specifies the command to be executed, and is passed as argument
zero. The remaining words are passed as arguments to the invoked command.

The environment for any simple command or function may be augmented temporarily
by prefixing it with variable assignments. These assignment statements affect
only the environment seen by that command.

::

    $ [var=value ...] command [arg ...]

The return value of a simple command is its exit status, or 128+n if the
command is terminated by signal n.  

Compound commands
-----------------

[[ expression ]]
    *Word splitting* and *pathname expansion* are not performed on the words
    between the '[[' and ']]'; *tilde expansion*, *parameter* and *variable
    expansion*, *arithmetic expansion*, *command substitution*,  *process
    substitution*, and *quote  removal* are performed.

    `Bash pitfalls: [ $foo = "bar" ]
    <https://mywiki.wooledge.org/BashPitfalls#A.5B_.24foo_.3D_.22bar.22_.5D>`_
