Sed
===

:Updated: : 2021/05/18


sed 的基本语法如下: ::

    sed [options ... ] [address]command[command options] [inputfile ...]

sed 可以同时执行多条命令，用换行符或者用分号分隔，或者使用多个 ``-e`` 参数： ::

    $ sed '/^foo/d; s/hello/world/'
    $ sed -e '/^foo/d' -e 's/hellow/world/'
    $ sed -f <(echo "/^foo/d; s/hello/world/")
    $ sed -f <(echo -e "/^foo/d\ns/hello/world/")

sed 在运行的时候，内部维护了两个 buffer，一个是 `pattern space`_ ，另一个是 `hold space`_ 。
sed 每次只能对一行数据进行处理，每次处理的时候会把整行的内容塞到 pattern space 中，
如果有必要的话，再通过 'h', 'H', 'g', 'G' 等命令保存到 hold space 中，
等处理完操作下一行的数据时又会清空这两个 buffer 中的内容。

1. Addresses
------------

如果只有一个 address，表示该 address 匹配到的行。
如果有两个 address，并用逗号分隔，表示从第一个 address 到第二个 address 匹配到的范围。

1.1 Number addresses
""""""""""""""""""""

``NUMBER``
    Specifying a line number will match only that line in the input.

    ::

        $ seq 3 | sed -n '2p'
        2

``$``
    Matches the last line of the last file of input.

    ::

        $ seq 3 | sed -n '$p'
        3

``FIRST~STEP``
    Matches every STEPth line starting with line FIRST.

    ::

        $ seq 3 | sed -n '1~2p'
        1
        3

1.2 Regex addresses
"""""""""""""""""""

``/REGEXP/`` (The '/' may be replaced by any other single character.)
    Matches the regular expression REGEXP.

    ::

        $ seq 3 | sed -n '/^[0-2]$/p'
        1
        2

2. Commands
-----------

**Note**: 为了便于理解，在使用的时候加上 ``--debug`` 参数可以看到 sed 的执行步骤。

2.1 Common commands
"""""""""""""""""""

``a <TEXT>``
    Append <TEXT> after line.

    ::

        $ seq 2 | sed 'a a'
        1
        a
        2
        a

``i <TEXT>``
    Insert <TEXT> before a line.

    ::

        $ seq 2 | sed 'i i'
        i
        1
        i
        2

``c <TEXT>``
    Replace lines with <TEXT>.

    ::

        $ seq 3 | sed '2 c c'
        1
        c
        3


``d``
    Delete the `pattern space`_; immediately start next cycle.

    ::

        $ seq 3 | sed '2d'
        1
        3

``p``
    Print out the pattern space.

    ::

        $ seq 3 | sed -n '2p'
        2

``N``
    Add a newline to the pattern space, then append the next line of input to
    the pattern space. If there is no more input then 'sed' exits without
    processing any more commands.

    ::

        $ seq 3 | sed -n 'N; p'
        1
        2

2.2 Hold space commands
"""""""""""""""""""""""

``g``
    Replace the contents of the pattern space with the contents of the hold
    space.

``G``
    Append a newline to the contents of the pattern space, and then append the
    contents of the hold space to that of the pattern space.

``h``
    (hold) Replace the contents of the hold space with the contents of the
    pattern space.

``H``
    Append a newline to the contents of the hold space, and then append the
    contents of the pattern space to that of the hold space.

2.3 Branching and flow Control commands
---------------------------------------

首先需要了解下 `label`_ ，label 即在 sed 代码中打上一个标记，稍后可以通过下面的三个命令进行跳转，有点类似 C 的 goto 语句。

``b [<LABLE>]``
    不管怎么样，马上跳转到 label

    ::

        $ seq 3 | sed -n 's/2/b/; b ; p'
        <return nothing>

``t [<LABEL>]``
    如果有 ``s///`` 命令执行成功，则立马跳转到 label

    ::

        $ seq 3 | sed -n 's/2/b/; t ; p'
        1
        3

``T [<LABEL>]``
    如果 ``s///`` 命令没有执行成功，则立马跳转到 label

    ::

        $ seq 3 | sed -n 's/2/b/; T ; p'
        b

2.4 Basic (BRE) and extended (ERE) regular expression
-----------------------------------------------------

BRE 和 ERE 的唯一区别是 ``? + () {} |`` 这几个特殊字符，
在 BRE 中需要加上 '\' 前缀在能有特殊含义（例如 '\?', '\(', '\)' 等），而在 ERE 中不需要这么做，其本身就又特殊含义。

2.5 Named classes of characters in bracket expressions
------------------------------------------------------

**Note**: These named classes must be used *inside* brackets themselves.

Incorrect example: ::

    $ echo 1 | sed 's/[:digit:]/X/'
    sed: character class syntax is [[:space:]], not [:space:]


Correct example: ::

     $ echo 1 | sed 's/[[:digit:]]/X/'
     X

References
----------

.. _pattern space:

patter space
    On every cycle, 'sed' reads one line from the input stream, removes any
    trailing newline, and places it in the pattern space.  Then all commands
    are executed and print the contents of pattern space to the output stream,
    adding back the trailing newline if it was removed. Then the next cycle
    starts for the next input line. Unless special commands (like 'D') are
    used, the pattern space is deleted between two cycles. 

.. _hold space:

hold space
    On the other hand, keeps its data between cycles (see commands 'h', 'H',
    'x', 'g', 'G' to move data between both buffers).

.. _label:

label
    Labels are defined with a colon followed by one or more letters (e.g.
    ':x').  If the label is omitted the branch commands restart the cycle.


(To find more, see ``info sed``)
