Perl
====

Context
-------

Scalar, List and Void Context
    Assignment is a little bit special in that it uses its left argument to
    determine the context for the right argument. Assignment to a scalar
    evaluates the right-hand side in scalar context, while assignment to an
    array or hash evaluates the righthand side in list context. Assignment to a
    list (or slice, which is just a list anyway) also evaluates the right-hand
    side in list context.

    https://perldoc.perl.org/perldata.html#Context

Scalar context

List context

Boolean Context
    A scalar value is true if it is not the null string "" or the number 0 (or
    its string equivalent, "0").

    A reference is always true because it represent an address that is never 0.

    An undefined value (often called ``undef``) is always false because it
    looks like either "" or 0, depending on whether you treat it as a string or
    a number.


References
----------

https://en.wikibooks.org/wiki/Perl_Programming
