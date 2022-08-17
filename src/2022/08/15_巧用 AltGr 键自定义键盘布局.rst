巧用 AltGr 键自定义键盘布局
===========================

:Published:  2022/08/15

.. meta::
    :description: 通过 AltGr 键，给键盘自定义一套 layer。

键盘上的上下左右键位不在核心区域，无奈每次都需要抬手去按，因而打字流畅度大打折扣。
有没有比较优雅的方案呢？ —— 当然有， `前文 </2018/12/15_CapsLock%20键重绑定.html>`_ 中我提到了 xmodmap 工具，可以用来自定义键位。

但问题是上下左右键共有四个键，映射到哪些键位比较合适呢？
仔细观察键盘上的每个按键，尤其是边边角角，想着能扣出几个位置来给上下左右“四兄弟”，奈何键盘这寸土寸金之地，哪还有它们的落脚之地。

好在看 xmodmap 的文档的时候，发现 keysym 的可以包含如下 6 种定义（不过在 ``xmodmap -pke`` 的输出结果中，发现不止 6 种） [#]_ ：

    Each keycode is followed by the keysym it is mapped to. Each keysym column in the table corresponds to a particular combination of modifier keys:
    
    1. Key
    2. Shift+Key
    3. Mode_switch+Key
    4. Mode_switch+Shift+Key
    5. ISO_Level3_Shift+Key
    6. ISO_Level3_Shift+Shift+Key

那么我就可以通过 Mode_switch 或者 ISO_Level3_Shift 这两个 modifier key 对键位映射新的含义。

这里解释下相关名词的含义：

- keycode: the numeric representation received by the kernel when a key or a mouse button is pressed.
- keysym: the value assigned to the keycode. For example, pressing a generates the keycode 38, which is mapped to the keysym 0×61, which matches a in the ASCII table.
- ISO_Level3_Shift: The AltGr key on non-US keyboards calls modifier ISO_Level3_Shift. (On US keyboards, the right-alt Alt_R has the same function as the left-alt Alt_L, which makes setting the layout as US international preferable.)
- Mode_switch: The Mode_switch modifier may be mapped by default to a key that is not on your keyboard.

另外，关于 modifier key，它可以用来修改键位原本的含义，通过 ``xev -event keyboard`` 命令的输出，可以直观的看出差异。
例如，原本仅按 a 键输出的是 "a"，这里 ``state 0x0`` 表示没有按任何 modifier key， ``keycode 38`` 表示 a 键的 keycode 为 38： ::

    KeyPress event, serial 28, synthetic NO, window 0x4600001,
        root 0x520, subw 0x0, time 357030121, (154,616), root:(155,617),
        state 0x0, keycode 38 (keysym 0x61, a), same_screen YES,
        XLookupString gives 1 bytes: (61) "a"
        XmbLookupString gives 1 bytes: (61) "a"
        XFilterEvent returns: False


而在按 a 键的同时按 shift 键，则会输出 "A"，这次 state 不再是 0x0，即表明 modifier key 被按下，而 0x1 则代表 shift 键。
另一方面可以发现 kecode 仍然是 38： ::

    KeyPress event, serial 28, synthetic NO, window 0x4600001,
        root 0x520, subw 0x0, time 357104060, (478,623), root:(479,624),
        state 0x1, keycode 38 (keysym 0x41, A), same_screen YES,
        XLookupString gives 1 bytes: (41) "A"
        XmbLookupString gives 1 bytes: (41) "A"
        XFilterEvent returns: False

通过这种方式，可以得到其它 modifer key 的 keycode，如果是多个 modifer key 的组合键，则 keycode 是它们的合：

+------------+-----------+
| Key        | Keycode   |
+============+===========+
| Shift      | 0x1       |
+------------+-----------+
| Ctrl       | 0x4       |
+------------+-----------+
| Alt        | 0x8       |
+------------+-----------+
| Ctrl+Shift | 0x5       |
+------------+-----------+
| Ctrl+Alt   | 0xc       |
+------------+-----------+

综上所述，通过 AltGr 键（即 ISO_Level3_Shift 键） [#]_ 加上其他按键的组合键可以对上下左右键重新映射。
但新的问题又来了，在 US 标准布局的键盘上，是没有 AltGr 键的，那么有没有可能通过软件层面将右侧的 Alt 键转化成 AltGr 键？
答案是肯定的，而且有两种方法：
其一是使用 ``setxkbmap -variant altgr-intl`` 命令，或是将如下配置添加到 */etc/X11/xorg.conf.d* 目录下 [#]_ ： ::

    Section "InputClass"
        Identifier "Keyboard Defaults"
        MatchIsKeyboard "yes"
        Driver "evdev"
        Option "XkbLayout" "us"
        Option  "XkbVariant" "altgr-intl"
    EndSection

最终，通过 AltGr 这个 modifier key，我将上下左右键分别映射到 ``AltGr+WSAD`` 这些组合键上。
其实，利用 AltGr 键完全可以做到给键盘重新映射一层自定义的 layer。

Thanks for reading :)

References
----------

.. [#] `ArchWiki: xmodmap <https://wiki.archlinux.org/title/xmodmap>`_
.. [#] `Wikipedia: AltGr key <https://en.wikipedia.org/wiki/AltGr_key#:~:text=AltGr (also Alt Graph) is,typographic marks and accented letters.>`_
.. [#] `Xorg: Using the US International (altgr-intl variant) Keyboard Layout <https://zuttobenkyou.wordpress.com/2011/08/24/xorg-using-the-us-international-altgr-intl-variant-keyboard-layout/>`_
