Perl
====

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


References
----------

https://en.wikibooks.org/wiki/Perl_Programming
