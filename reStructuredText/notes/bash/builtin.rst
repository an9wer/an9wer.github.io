Builtin
=======

set
---

pipefail
    The return status of a pipeline is the exit status of the last command, un
    less the pipefail option is enabled. If pipefail is enabled, the pipeline's
    return status is the value of the last (rightmost) command  to exit with  a
    non-zero status, or zero if all commands exit successfully.  


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
