Caps_Lock key 重绑定
====================

:Published: : 2018/12/15

.. meta::
    :description: Ctrl 是 Bash 和 Vim 中常用的按键，但其位于键盘的左下角，按起
        来实在不舒服，所以我通过 xmodmap 将其重新绑定到了 Caps_Lock 键上。

大概是在两年前，刷知乎的时候看到用手掌外侧按 Ctrl 键的方法。
当时刚学 Linux，此方法在 Linux 下简直就是神技，
因为在 Bash 中默认使用了 Emacs 的模式进行命令的编辑，
例如：Ctrl-a 将光标移动到行首，Ctrl-e 将光标移动到行末，Ctrl-b 将光标往左移动一个字母，等等；
而在 Vim 里也经常会用到 Ctrl 的组合键，
例如：Ctrl-[ 退出插入模式，其作用相当于 Esc 键。
使用 Ctrl 的组合键的好处除了其本身的功能外，还有重
要的一点就是提高打字的效率，我们的双手可以始终保持在键盘中心区域，避免抬手去按
一些位置比较靠边的键。

这么好的技能，却也有一个缺点，最近我也是深感苦恼。
因为左 Ctrl 键处于键盘的左下角边缘，长时间高频率使用手掌外侧按压，其方正的棱角会导致我的手掌逐渐产生疼痛感。

所以有没有什么好的办法能解决这个问题呢？
这一点的话 Emacs 用户应该是比较有心得的（因为他们经常要按 Ctrl 键啊）。
Emacs 用户通常将 Caps_Lock 键与 Ctrl 键互换，毕竟小拇指按 Caps_Lock 还是比较舒服的。
开源之父 Richard Stallman 用的就是 HHKB 这种 Ctrl 在 Caps_Lock 位置的键盘。
当然我肯定不会因为这个原因去买一把 2000 多人民币的 HHKB。

在 Linux 下有个 xmodmap 命令，可以修改键位。
于是花了点时间了解了下这条命令，发现其语法规则还是挺简单的，
新建 *~/.Xmodpad* 文件，在里面写入如下内容： ::

    clear Lock
    keysym Caps_Lock = Control_L
    add Control = Control_L

该命令表示取消 Caps_Lock 键原有的功能，将其重新绑定到 Control 键。
之后执行 ``xmodmap ~/.Xmodpad`` 命令，键位即修改成功。
不过这样以后，我就得适应 Caps_Lock 的按键方法。
今天尝试了一天，经常会和 Shift 键搞混在一起，看来得适应一段时间了，呵呵。

Updated 2018/12/24
------------------

在知乎看到了 `这篇回答 <https://www.zhihu.com/question/22127282/answer/42905465>`_ —— 将键帽反过来装在键盘上。
这还真是个好办法，于是这两天又用 xmodmap 重新将键位映射了一遍，现在被我修改的键位如下：

+-----------+-----------+
|           | Bind to   |
+===========+===========+
| Caps_Lock | Return    |
+-----------+-----------+
| Alt_R     | backslash |
+-----------+-----------+
| Menu      | BackSpace |
+-----------+-----------+
| Super_R   | Escape    |
+-----------+-----------+

配置详见 `这里 <https://github.com/an9wer/werice/tree/master/xmodmap>`_ 。

Thanks for reading :)
