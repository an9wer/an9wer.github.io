CapsLock 键重绑定
=================

:Published: 2018/12/15

.. meta::
    :description: Ctrl 键是 Bash 和 Vim 中常用的按键，但其位于键盘的左下角，按起
        来实在不舒服，因此通过 xmodmap 将其重新绑定到了 Caps_Lock 键上。

大概是在两年前，刷知乎的时候看到用手掌外侧按 Ctrl 键的方法。

此方法在 Linux 下简直就是神技，
因为在 Bash 中，快捷键默认与 Emacs 一致，
例如：Ctrl-a 将光标移动到行首，Ctrl-e 将光标移动到行末，Ctrl-b 将光标往左移动一个字母，等等；
另外，在 Vim 里也经常会用到 Ctrl 的组合键，
例如：Ctrl-[ 退出插入模式，其作用相当于 Esc 键。
使用 Ctrl 的组合键的好处除了其本身的功能外，还可以提高打字效率，双手能够始终保持在键盘中心区域。

如此神技，却也有一个缺点 —— 
Ctrl 键处于键盘的左下角边缘，长时间高频率使用手掌外侧按压，其尖尖的棱角会逐渐致疼我的手掌。

所以有没有什么好的办法能解决这个问题呢？
这一点的话 Emacs 用户应该是比较有心得的，因为他们经常要按 Ctrl 键。
Emacs 用户通常将 CapsLock 键与 Ctrl 键互换，毕竟小拇指按 CapsLock 还是比较舒服的。
开源之父 Richard Stallman 用的就是 HHKB 这种 Ctrl 在 CapsLock 位置的键盘。
当然我肯定不会因为这个原因去买一把 2000 多人民币的 HHKB。

在 Linux 下有个工具 —— xmodmap，它可以帮助我们自定义键位。
例如，取消 CapsLock 键原有的功能，将其重新绑定到 Control 键： ::

    clear Lock
    keysym Caps_Lock = Control_L
    add Control = Control_L

虽说是修改成功了，但新的键位还是比较难适应，经常会和 Shift 键搞混在一起，看来得适应一段时间了，呵呵。

Updated 2018/12/24
------------------

在知乎看到了 `一篇回答 <https://www.zhihu.com/question/22127282/answer/42905465>`_ —— 将键帽反过来装在键盘上。
这还真是个好办法，于是用 xmodmap 重新映射了键位：

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
