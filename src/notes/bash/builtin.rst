.. meta::
    :robots: noindex

Bash Builtin
============

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


getopts
-------

::

    getopts optstring name [args]

optstring
    Contains the option characters to be recognized; if a character is followed
    by a *colon*, the option is expected to have an argument, which should be
    seperated from it by white space.

name
    Each time getopts is invoked, it places the next option in the shell
    variable 'name'.

OPTIND
    Stores the index of the next argument, its initial value is 1. The shell
    doesn't reset OPTIND automatically; it must be manually reset.

OPTARG
    Stores the current argument.

Silent mode
    When the first character of 'optstring' is a *colon*, the getopt is silent.

When the end of options is encountered, getopts exits with a return value
greater than zero. 'OPTIND' is set to the index of the first non-option
argument, and 'name' is set to ?.

If an invalid option is seen, getopts places ? into 'name' and, if not silent,
prints an message and unset OPTARG. if getopts is silent, the option character
found is placed in 'OPTARG' and no diagnostic message is printed.

If a required argument is not found, and getopts is not silent, a question mark
(?) is placed in 'name', 'OPTARG' is unset. and a deagnostic message is
printed. If getopts is silent, the a colon (:) is placed in 'name' and 'OPTARG'
is set to the otpion character found.

