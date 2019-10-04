Vim Map
=======

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

To avoid the abbreviation in Insert mode: Type *CTRL-V* before the character
that would trigger the abbreviation. (E.g. CTRL-V <Space>.  Or type part of
the abbreviation, exit insert mode with <Esc>, re-enter insert mode with "a"
and type the rest.)

To avoid the abbreviation in Command-line mode: Type *CTRL-V* twice somewhere
in the abbreviation to avoid it to be replaced.  A *CTRL-V* in front of a
normal character is mostly ignored otherwise.

:ab[breviate]
    List all abbreviations.

:ab[breviate] {lhs}
    List the abbreviations that start with {lhs}.

:ab[breviate] [<expr>] [<buffer>] {lhs} {rhs}
    Add abbrevia for {lhs} to {rhs}. If {lhs} already existed it is replaced
    with the new {rhs}. {rhs} may contain spaces.

:ca[bbrev] [<expr>] [<buffer>] [lhs] [rhs]
    Same as ":ab[breviate]", but for Command-line mode only.

:ia[bbrev] [<expr>] [<buffer>] [lhs] [rhs]
    Same as ":ab[breviate]", but for Insert mode only.
