Perl
====

Scalar, List and Void Context
    Assignment is a little bit special in that it uses its left argument to
    determine the context for the right argument. Assignment to a scalar
    evaluates the right-hand side in scalar context, while assignment to an
    array or hash evaluates the righthand side in list context. Assignment to a
    list (or slice, which is just a list anyway) also evaluates the right-hand
    side in list context.

    https://perldoc.perl.org/perldata.html#Context
