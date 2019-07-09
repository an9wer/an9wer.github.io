Sed
===

See *info sed*

'sed' commands follow this syntax:

::

    [addr]X[options]

-   [addr]: is optional line address, it specify lines to be executed.

-   X: is a single-letter 'sed' command.

-   [options]: are used for some 'sed' commands.

**Note**: Commands within a SCRIPT or SCRIPT-FILE can be separated by
semicolons (';') or newlines (ASCII 10).

::

    sed '/^foo/d; s/hello/world/'

Equals to:

::

    sed -e '/^foo/d' -e 's/hellow/world/'

Equals to:

::

    sed -f <(echo "/^foo/d; s/hello/world/")

Equals to:

::

    sed -f <(echo -e "/^foo/d\ns/hello/world/")


Basic (BRE) and extended (ERE) regular expression
-------------------------------------------------

In GNU 'sed', the only difference between basic and extended regular
expressions is in the behavior of a few special characters: '?', '+',
parentheses, braces ('{}'), and '|'.

With basic (BRE) syntax, these characters do not have special meaning
unless prefixed with a backslash ('\'); While with extended (ERE) syntax
it is reversed: these characters are special unless they are prefixed
with backslash ('\').

Named classes of characters in bracket expressions
--------------------------------------------------

**Note**: These named classes must be used *inside* brackets themselves.

Correct usage:

::

     $ echo 1 | sed 's/[[:digit:]]/X/'
     X

Incorrect usage:

::

    $ echo 1 | sed 's/[:digit:]/X/'
    sed: character class syntax is [[:space:]], not [:space:]


