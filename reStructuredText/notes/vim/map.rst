Map
===

See `:h map.txt`

<expr>
    The expression is evaluated to obtain the {rhs} that is used.

    See `:h map-<expr>`

<buffer>
    The mapping/abbreviation is effective in the current buffer only.

    See `:h map-<buffer>`

Abbreviations
-------------

Abbreviations are used in Insert mode, Replace mode and Command-line mode.

Abbreviations are never recursive.

:ab[breviate]
    List all abbreviations.

:ab[breviate] {lhs}
    List the abbreviations that start with {lhs}.

:ab[breviate] [<expr>] [<buffer>] {lhs} {rhs}
    Add abbrevia for {lhs} to {rhs}. If {lhs} already existed it is replaced
    with the new {rhs}. {rhs} may contain spaces.

