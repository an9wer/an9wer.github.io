.. meta::
    :robots: noindex

Bc
==

Numbers
-------

The most basic element in 'bc' is the number. There are two attributes of
numbers, the length and the scale.  The length is the total number of digits
used by 'bc' to represent a number and the scale is the total number of decimal
digits after the decimal point. (For example, .000001 has a length of 6 and
scale of 6, while 1935.000 has a length of 7 and a scale of 3.)

Variables
---------

Special variables:

-   SCALE: How some operations use digits after the decimal point.

-   IBASE: the conversion base for input numbers.

-   OBASE: the conversion base for output numbers.

-   LAST: the value of the last printed number.

Comments
--------

Multiple lines comment
    starts with the characters ``/*`` and ends with the characters ``*/``

Single line comment
    starts at a ``#`` cahracter and continues to the next end of the line

Expression
----------

VAR = expr
    The variable is assigned the value of the expression.

Statements
----------

EXPRESSION
    If the expression starts with ``<variable> <assignment> ...``, it is
    considered to be an assignment statement.

    If the expression is not an assignment statement, the expression is
    evaluated and printed to the output. After the number is printed, a
    newline is printed.

STRING
    The string is printed to the output. Strings start with a double quote
    character and contain all characters until the next double quote character.

    All characters are taken literally, including any newline.

halt
    causes the 'bc' processor to quit only when it is executed.

quit
    causes the 'bc' processor to quit.
