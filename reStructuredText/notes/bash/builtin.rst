Builtin
=======

set
---

::

    set [-abefhkmnptuvxBCHP] [-o option-name] [--] [arg ...]

**Note**: Using + rather than - causes these flags to be turned off.

-v
    Print shell input lines as they are read.

    ::

        $ set -v

        $ cat <<EOF
        cat <<EOF
        > 1
        1
        > 2
        2
        > EOF
        EOF
        1
        2

-x
    Print commands and their arguments as they are executed.

    ::

        $ set -x

        $ echo 123
        + echo 123
        123

        $ cat <<EOF
        > 1
        > 2
        > EOF
        + cat
        1
        2

pipefail
    The return status of a pipeline is the exit status of the last command,
    unless the pipefail option is enabled. If pipefail is enabled, the
    pipeline's return status is the value of the last (rightmost) command  to
    exit with a non-zero status, or zero if all commands exit successfully.  

\-\-
    Assign any remaining arguments to the positional parameters. If there are
    no remaining arguments, the positional parameters are unset.


Shopt
-----

Options
"""""""

`-p`
    print each shell option with an indication of its status

`-s`
    enable OPTNAME

`-u`
    disable OPTNAME


Optnames
""""""""

globstar
    If set, the pattern ** used in a pathname expansion context will match all
    files and zero or more directories and subdirectories.  If the pattern is
    followed  by  a /, only directories and subdirectories match.
