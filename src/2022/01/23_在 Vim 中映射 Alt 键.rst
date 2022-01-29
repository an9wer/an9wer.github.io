在 Vim 中映射 Alt 键
====================

:Published: 2022/01/23

.. meta::
    :description: 近来想在 vim 的 command mode 中使用与 readline 的 emacs mode 相似的功能键，
        例如 ``alt-f`` 向前移动一个 word， ``alt-b`` 向后移动一个 word。这该如何配置呢？

（首先声明 Alt 键一般来说即所谓的 Meta 键）

近来想在 vim 的 command mode 中使用与 readline 的 emacs mode 相似的功能键，
例如 ``alt-f`` 向前移动一个 word， ``alt-b`` 向后移动一个 word。

本以为只要在 *~/.vimrc* 文件中加上如下两行简单的配置： ::

    cnoremap <M-b> <S-Left>
    cnoremap <M-f> <S-Right>

但结果这两行配置并没有起作用，看来我还是 too native！

一番搜索后，在 vim 的文档中（ ``:h map-alt-keys`` ）找到了答案：

    By default Vim assumes that pressing the ALT key sets the 8th bit of a typed character.
    Most decent terminals can work that way, such as xterm, aterm and rxvt.
    If your <A-k> mappings don't work it might be that the terminal is prefixing the character with an ESC character.
    But you can just as well type ESC before a character,
    thus Vim doesn't know what happened (except for checking the delay between characters, which is not reliable).

原来在默认情况下，vim 会认为 Alt 键是用来 set 8th bit of a typed character，但这同时也需要 terminal 的支持。
而我目前所使用的 st terminal 显然不是这样处理 Alt 键的，而是将 Alt 键当成 Esc 键在组合键中作为前缀使用。

- 什么是 set 8th bit of a typed character？

此时 Alt 键相当于 shift 键的一个扩展，可以用来输入 Latin-1 中 160 到 255 之间的字符 [#]_ 。
例如： 按下 ``alt-a`` 得到的是 á，按下 ``alt-b`` 得到的是 â，按下 ``alt-c`` 得到的是 ã，等等。

- 什么是将 Alt 键当成 Esc 键在组合键中作为前缀使用？

这种情况下，按 Alt 键相当于按 Esc 键，
不信可以在 bash 中试试按 ``alt-f`` 键与先按一个 ``Esc`` 键再按一个 ``f`` 键的效果是一样的。
这其实是由 readline 设定的（ ``man readline`` ）：

    prefix-meta (ESC)
        Metafy the next character typed.  ESC f is equivalent to Meta-f.

因此，解决 vim 中 Alt 键的映射问题也有两种方法。

方法一
------

设置 st terminal 支持将 Alt 键用来 set 8th bit of a typed character。
如何设置呢？说来还得用到 terminfo/termcap。

在 st 项目源码中，有个 *st.info* 文件，其内容即是 terminfo 配置，其中的 ``st-meta-256color`` 引起了我的注意： ::

    st-meta-256color| simpleterm with meta key and 256 colors,
            use=st-256color,
            km,
            rmm=\E[?1034l,
            smm=\E[?1034h,
            rs2=\E[4l\E>\E[?1034h,
            is2=\E[4l\E>\E[?1034h,

对照 ``man terminfo`` 文档中的说明，
得知 ``km`` 即表示 terminal 支持 meta mode，
而 ``rmm`` 和 ``smm`` 分别代表关闭和开启 meta mode 的 terminal code。
这正是我想要的，那么如何才能使用 ``st-meta-256color`` 的 terminfo 呢？

首先，需要使用 tic 命令将 *st.info* 源码文件转化成 terminfo 可识别的二进制文件： ::

    $ tic -sx st.info

tic 命令默认会将结果文件置于 ``$HOME/.terminfo`` 目录中，
使用 ``infocmp st-meta-256color`` 命令也能找到该文件。
但重启 st 之后发现没有任何变化。
这是为何？原因是 TERM 环境变量依然是先前的 ``st-256color`` ： ::

    $ echo $TERM
    st-256color

所以还得修改 st 的 *config.h* 文件，将 termname 设置成 ``st-meta-256color`` ，然后重新编译： ::

    $ vim config.h
        char *termname = "st-meta-256color";

这下重启 st 后，``st-meta-256color`` 的 terminfo 终于生效了，
但要启动 meta mode，还需键入 ``smm`` 的 terminal code： ::

    $ echo -e '\E[?1034h'

之后再通过开头提到的 *~/.vimrc* 中的两行配置： ::

    cnoremap <M-b> <S-Left>
    cnoremap <M-f> <S-Right>

即可在 vim 中成功映射 Alt 键。

但是，此方法有个很大的副作用 —— 不管是在 vim 还是 readline 中都需要重新定义所有 Alt 键相关的功能键，
如果没有重新定义则按下 Alt 键相关的功能键得到就是 á â 之流的拉丁字母啦！

难不成我每次在使用 vim 前先 ``echo -e '\E[?1034h'`` 开启 meta mode，
使用完 vim 之后再 ``echo -e '\E[?1034l'`` 关闭 meta mode？
甚烦！

方法二
------

既然 st terminal 是将 Alt 键当成 Esc 键在组合键中作为前缀使用，那么将计就计，
把 ``<M-b>`` 和 ``<M-f>`` 的 terminal code 分别定义成 ``^[b`` 和 ``^[f`` 即可 [#]_ ： ::

    " 映射 keysym 到 terminal code
    set <M-b>=^[b
    set <M-f>=^[f

    " 自定义 command mode 中的 key
    cnoremap <M-b> <S-Left>
    cnoremap <M-f> <S-Right>

将上述配置添加到 *~/.vimrc* 中，也能成功映射 Alt 键。

但是，此方法也同样有个副作用 —— Esc Delay [#]_ 。不过要解决这个副作用好在可以比较简单地解决，只需要再添加一行配置： ::

    set ttimeoutlen=50

Thanks for reading :)

See Also
--------

- `What is bash's meta key? <https://unix.stackexchange.com/a/266490/474814>`_

References
----------

.. [#] `Alt-keys do not work in bash <https://invisible-island.net/ncurses/ncurses.faq.html#bash_meta_mode>`_
.. [#] ``:h set-termcap``
.. [#] `关于 Vim 的 Esc Delay </2022/01/23_关于%20Vim%20的%20Esc%20Delay.html>`_
