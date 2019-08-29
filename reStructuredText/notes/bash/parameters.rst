Parameters
==========

A variable may be assigned to by a statement of the form:

::

    name=[value]

**Note**: Word splitting is not performed, with the exception of "$@".


Special parameters
------------------

\*
    Expands to the positional parameters, starting from one.

    When the expansion is not within double quotes, each positional parameter
    expands to a separate word. In contexts where it is performed, those words
    are subject to further word splitting and pathname expansion.

    ::

        $ set -- 1 2 " 3 4 "
        $ foo=( $* )
        $ declare -p foo
        declare -a foo=([0]="=" [1]="1" [2]="2" [3]="3" [4]="4")

    When the expansion occurs within double quotes, it expands to a single word
    with the value of each parameter separated by the first character of the
    IFS special variable. (If IFS is unset, the parameters are separated by
    spaces.  If IFS is null, the parameters are joined without intervening
    separators.)

    ::

        $ set -- 1 2 " 3 4 "
        $ bar=( "$*" )
        $ declare -p bar
        declare -a bar=([0]="1 2  3 4 ")

\@
    Expands to the positional parameters, starting from one.

    In contexts where word splitting is performed, this expands each positional
    parameter to a separate  word; if not within double quotes, these words are
    subject to word splitting.

    ::

        $ set -- 1 2 " 3 4 "
        $ foo=( $@ )
        $ declare -p foo
        declare -a foo=([0]="1" [1]="2" [2]="3" [3]="4")

    In contexts where word splitting is not performed, this expands to a single
    word with each positional parameter separated by a space. When the
    expansion occurs within double quotes, each parameter expands to a separate
    word.

    ::

        $ set -- 1 2 " 3 4 "
        $ bar=( "$@" )
        $ declare -p bar
        declare -a bar=([0]="1" [1]="2" [2]=" 3 4 ")

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

