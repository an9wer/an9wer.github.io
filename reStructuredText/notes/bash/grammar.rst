Bash Grammar
============

Compound commands
-----------------

[[ expression ]]
    *Word splitting* and *pathname expansion* are not performed on the words
    between the '[[' and ']]'; *tilde expansion*, *parameter* and *variable
    expansion*, *arithmetic expansion*, *command substitution*,  *process
    substitution*, and *quote  removal* are performed.

    `Bash pitfalls: [ $foo = "bar" ]
    <https://mywiki.wooledge.org/BashPitfalls#A.5B_.24foo_.3D_.22bar.22_.5D>`_
