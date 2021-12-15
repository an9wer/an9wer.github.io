less
====

:Updated: : 2021/12/15

**注意** ： 
下面的命令中，如果出现用空格分隔的两种命令，二者的作用相同。

标记命令
    ``m``
        Followed by any lowercase or uppercase letter, marks the first
        displayed line with that letter.

    ``'``
        Followed by any lowercase or uppercase letter, returns to the position
        which was previously marked with that letter.  -   

    ``ESC-m``
        Followed by any lowercase or uppercase letter, clears the mark
        identified by that letter.

文件命令
    ``:e [filename]`` ``E [filename]``
        Examine a new file. 

    ``:n``
        Examine the next file.

    ``:p``
        Examine the previous file.

    ``:d``
        Remove the current file from the list of files.

日志命令
    ``s [filename]``
        Save the input to a file.
