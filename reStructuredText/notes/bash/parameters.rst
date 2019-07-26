Parameters
==========

Special parameters
------------------

\-
    Expands to the current option flags as specified upon invocation, by the
    set builtin command, or those set by the shell itself (such as the *-i*
    option).

    In *bashrc*, if not running interactively, don't do anything:
    ::

        [[ $- != *i* ]] && return
        
\$
    Expands to the process ID of the shell.  In a () subshell, it expands to
    the process ID of the current shell, not the subshell.

    ::

        $ echo $$
        21514
        $ echo $(echo $$)
        21514
        $ echo $(echo $(echo $$))
        21514


Variables
---------

RANDOM
    Each time this parameter is referenced, a random integer between 0 and
    32767 is generated.
     
BASH_SOURCE
    An array variable whose members are the source filenames. `$BASH_SOURCE[0]`
    is the current script name, sourced from `$BASH_SOURCE[1]`, and so on.

    https://stackoverflow.com/questions/59895/get-the-source-directory-of-a-bash-script-from-within-the-script-itself

    https://stackoverflow.com/a/35006505

