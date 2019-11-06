Sed
===

See ``info sed``


``sed`` is a stream editor and follows this syntax: ::

    sed [options ... ] [address]command[command options] [inputfile ...]

**Note**: Multiple commands are accpeted, but ned to separated by semicolons
(';') or newlines (ASCII 10), or specified with '-e' or '-f' options:  ::

    sed '/^foo/d; s/hello/world/'

Equals to: ::

    sed -e '/^foo/d' -e 's/hellow/world/'

Also equals to: ::

    sed -f <(echo "/^foo/d; s/hello/world/")

And also equals to: ::

    sed -f <(echo -e "/^foo/d\ns/hello/world/")

Options
-------

--debug
    Debug mode


Address
-------

NUMBER
    Specifying a line number will match only that line in the input. (**Note**
    that 'sed' counts lines continuously across all input files unless '-i' or
    '-s' options are specified.)

\$
    Matches the last line of the last file of input, or the last line of each
    file when the '-i' or '-s' options are specified.

FIRST~STEP
    Matches every STEPth line starting with line FIRST.

/REGEXP/
    Matches the regular expression REGEXP.

\%REGEXP% (The '%' may be replaced by any other single character.)
    Matches the regular expression REGEXP, but allows one to use a different
    delimiter than '/'.

/REGEXP/I
    The 'I' modifier to regular-expression matching is a GNU extension which
    causes the REGEXP to be matched in a case-insensitive manner.

/REGEXP/M
    The 'M' modifier to regular-expression matching is a GNU 'sed' extension
    which directs GNU 'sed' to match the regular expression in 'multi-line'
    mode.

-   An address range can be specified by specifying two addresses separated by
    a comma (','). An address range matches lines starting from where the first
    address matches, and continues until the second address matches.


Command
-------

**Note**: use ``--debug`` option to see what happened when you are confused.

a <TEXT>
    Append <TEXT> after line.

i <TEXT>
    Insert <TEXT> before a line.

c <TEXT>
    Replace (change) lines with <TEXT>.

d
    Delete the `pattern space`_; immediately start next cycle.

D
    If pattern space contains newlines, delete text in the pattern space up to
    the first newline, and restart cycle with the resultant pattern space,
    without reading a new line of input.

    If pattern space contains no newline, start a normal new cycle as if the
    'd' command was issued.

p
    Print out the pattern space.

l
    Print the pattern space in an `unambiguous form`_. 

g
    Replace the contents of the pattern space with the contents of the `hold
    space`_.

G
    Append a newline to the contents of the pattern space, and then append the
    contents of the hold space to that of the pattern space.

h
    (hold) Replace the contents of the hold space with the contents of the
    pattern space.

H
    Append a newline to the contents of the hold space, and then append the
    contents of the pattern space to that of the hold space.

.. _unambiguous form:

-   unambiguous form:

    Non-printable characters (and the \\ character) are printed in C-style
    escaped form; long lines are split, with a trailing \\ character to
    indicate the split; the end of each line is marked with a $. 

.. _pattern space:

-   patter space

    On every cycle, 'sed' reads one line from the input stream, removes any
    trailing newline, and places it in the pattern space.  Then all commands
    are executed and print the contents of pattern space to the output stream,
    adding back the trailing newline if it was removed. Then the next cycle
    starts for the next input line. Unless special commands (like 'D') are
    used, the pattern space is deleted between two cycles. 

.. _hold space:

-   hold space

    On the other hand, keeps its data between cycles (see commands 'h', 'H',
    'x', 'g', 'G' to move data between both buffers).

    
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

Incorrect usage: ::

    $ echo 1 | sed 's/[:digit:]/X/'
    sed: character class syntax is [[:space:]], not [:space:]


Correct usage: ::

     $ echo 1 | sed 's/[[:digit:]]/X/'
     X

