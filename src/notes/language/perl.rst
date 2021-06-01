.. meta::
    :robots: noindex

Perl
====

Data
----

Perl has three built-in data types: scalars, arrays of scalars, and associative
arrays of scalars, known as "hashes".

Values are usually referred to by name, or through a named reference. The first
character of the name tells you to what sort of data structure it refers. The
rest of the name tells you the particular value to which it refers. 

1. Scalar values are always named with '$', even when referring to a scalar
that is part of an array or a hash. ::

    $days           # the simple scalar value "days"
    $days[28]       # the 29th element of array @days
    $days{'Feb'}    # the 'Feb' value from hash %days
    $#days          # the last index of array @days

1.  Entire arrays (and slices of arrays and hashes) are denoted by '@'. ::

    @days           # ($days[0], $days[1],... $days[n])
    @days[3,4,5]    # same as ($days[3],$days[4],$days[5])
    @days{'a','c'}  # same as ($days{'a'},$days{'c'}

1.  Entire hashes are denoted by '%'. ::

    %days           # (key1, val1, key2, val2 ...)

1.  Subroutines are named with an initial '&', though this is optional when
unambiguous.

1.  Symbol table entries can be named with an initial '*'.

Perl arrays and hashes are internally one-dimensional. That is, their elements
can hold only scalar values (string, numbers, and references). When we use a
phrase like "array of arrays", we really mean "array of references to arrays",
just as when we say "hash of functions", we really mean "hash of references to
subroutines".


Interpolation
-------------

The following escape sequences are available in constructs that interpolate,
and in transliterations whose delimiters aren't single quotes: ::

    Sequence     Note  Description
    \t                  tab               (HT, TAB)
    \n                  newline           (NL)
    \r                  return            (CR)
    \f                  form feed         (FF)
    \b                  backspace         (BS)
    \a                  alarm (bell)      (BEL)
    \e                  escape            (ESC)
    \x{263A}     [1,8]  hex char          (example: SMILEY)
    \x1b         [2,8]  restricted range hex char (example: ESC)
    \N{name}     [3]    named Unicode character or character sequence
    \N{U+263D}   [4,8]  Unicode character (example: FIRST QUARTER MOON)
    \c[          [5]    control char      (example: chr(27))
    \o{23072}    [6,8]  octal char        (example: SMILEY)
    \033         [7,8]  restricted range octal char  (example: ESC)

Array variables are interpolated into double-quote strings by joing all
elements of the array with the separator specified in the ``$"`` variable: ::

    my $temp = join( $", @ARGV);
    print $temp;

    print "@ARGV";

Context
-------

https://perldoc.perl.org/perldata.html#Context

Scalar context
    Assignment to a scalar variable, or to a scalar element of an array or
    hash, evaluates the righthand side in a scalar context: ::

        $x = func();
        $x[1] = func();
        $x{"1"} = func();

List context
    Assignment to an array or a hash, or to a slice either, evaluates the
    righthand side in a list context, even if the slice picks out only on
    element: ::

        @x = func();
        @x[1] = func();
        %x = func();

    Assignment to a list of scalars also provides list context to the righthand
    side, even if there's only one element in the list: ::

        ($x, $y, $z) = func();
        ($x) = func();

Boolean Context
    A scalar value is true if it is not the null string "" or the number 0 (or
    its string equivalent, "0"). A reference is always true because it
    represent an address that is never 0. An undefined value (often called
    ``undef``) is always false because it looks like either "" or 0, depending
    on whether you treat it as a string or a number.

    A list value is true if it  ther are any elements in it.


::

    $foo = ("one", "two", "three"); # The value of $foo is "three" (the last element of list)

    @bar = ("one", "two", "three"); # The value of @bar is ("one", "tow", "three")

    $foo = @bar;                    # The value of $foo is 3 (the length of array)

Operators
---------

Quote and Quote-like Operators
    **Note**: In the following table, a ``{}`` represents any pair of
    delimiters you choose: ::

        Customary   Generic        Meaning             Interpolates
        ''          q{}            Literal             no
        ""          qq{}           Literal             yes
        ``          qx{}           Command             yes*
                    qw{}           Word list           no
        //          m{}            Pattern match       yes*
                    qr{}           Pattern             yes*
                    s{}{}          Substitution        yes*
                    tr{}{}         Transliteration     no
                    y{}{}          Transliteration     no
                    <<EOF          here-doc            yes*

            * unless the delimiter is ''.
    

List operators (Leftward)
    If any list operator (such as ``print``) or any named unary operator (such
    as ``chdir``) is followed by a left parenthesis as the next token (ignoring
    whitespace), the operator and its parenthesized arguments are given highest
    precedence, as if it wre a normal function call. ::

        open($fh, ">", "logfile") or die;   # OK
        open($fh, ">", "logfile") || die;   # OK

List operators (Rightward)
    The right side of a list operator governs all the list operator's
    arguments, which are comma separated, so the precedence of a list operator
    is lower than a comma.  ::

        open $fh, ">", "logfile" || die;    # Wrong
        open $fh, ">", "logfile" or die;    # OK
        
Syntax
------

BLOCK ``{}`` by itself (labeled or not) is semantically equivalent to a loop
that executes once. Thus you can use any of the loop control statements in it
to leave or restart the block. (Note that this is NOT true in ``eval{}``,
``sub{}``, or contrary to popular belief ``do{}`` blocks, which do NOT count as
loops.) The continue block is optional. ::

    SWITCH: {
        if (/^abc/) { $abc = 1; last SWITCH; }
        if (/^def/) { $def = 1; last SWITCH; }
        if (/^xyz/) { $xyz = 1; last SWITCH; }
        $nothing = 1;
    }

    if (1) { {
        last;
        print 1;        # Not do
    } }

In ``while`` statement, if the condition expression is based on any of a group
of iterative expression types then it gets some magic treatment. The affected
iterative expression types are ``readline EXPR``, the ``<FILEHANDLE>`` input
operator, ``readdir DIRHANDLE``, ``glob EXPR``, the ``<PATTERN>`` globbing
operator, and ``each HASH``.  If the condition expression is one of these
expression types, then the value yielded by the iterative operator will be
implicitly assigned to ``$_`` . If the condition expression is one of these
expression types or an explicit assignment of one of them to a scalar, then the
condition actually tests for definedness of the expression's value, not for its
regular truth value. ::

    while (<>) { }
    while (defined($line = <ARGV>)) { }


Built-in functions
------------------

open
    Returns true when it succeeds and ``undef`` otherwise. If the ``open``
    starts up a pipe to a child process, the return value will be the process
    ID of that new process.

    If you supply an undefined variable for the filehandle, perl will
    automaticall define that variable for you, that is, autovivifying it to
    contain a proper filehandle reference. One advantage of this is that the
    filehandle will be closed automatically when there are no futher references
    to it, typically when the variable goes out of scope: ::

        {
            my $fh;
            open $fh, ">", "logfile"
                or die "Can't create logfile: $!";
        }   # $fh closed here

References
----------

https://en.wikibooks.org/wiki/Perl_Programming
