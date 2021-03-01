Fcitx VS Ibus
=============

起因是装了 Fedora 30 之后发现其自带了中文输入法，了解之后发现是 Ibus，暗黑的配
色一下子吸引了我，更重要的是输入手感也很棒。

于是在工作的电脑上安装了 Ibus，体验了一阵。接下来就针对我个人的使用习惯，简单将
Ibus 与我之前一直使用的 Fcitx 做一个对比：

**Fcitx**:

-   配置项复杂

-   可以使用 Shift_R 键切换中英文输入法

-   从某个应用切换到另一个应用不会保留输入法，但同应用之间会保留。

-   项目不再维护

**Ibus**:

-   配置项简单

-   不可以使用 Shift_R 键 (只能 Shift）切换中英文输入法

-   输入法状态为全局，从某个应用切换到另一个应用会保留输入法
  
-   项目仍在更新维护


输入法引擎方面，这次也顺带尝试了 ibus-libpinyin 和 ibus-rime：

**ibus-libpinyin**:

-   在中文输入法状态下按 shift 键会 commit 已经输入的字母，然后切换成英文输入法

-   配置简单（GUI），功能够用
  
**ibus-rime**:

-   在中文输入法状态下按 shift 键会 commit 已经输入的字母的第一个中文选项，然后
    切换成英文输入法

-   配置麻烦（使用文件进行配置，无 GUI，比较符合我的风格），功能很强


另外，在文章的开头也提到了 Ibus 的皮肤是吸引我的一点，但在 Arch 中，我还真不知
道如何配置 Ibus 的皮肤？

对比之后，我选择的方案是 Ibus + ibus-rime，并通过比较 hack 的方式，将 rime 切换
输入法的按键设置成了 Shift_R。

Update 2019/09/04
-----------------

尝试修改 ibus 的配色，搜了一圈，只发现了修改 icon 颜色的方法： ::

    $ gsettings set org.freedesktop.ibus.panel xkb-icon-rgba '#415099'

只好暂且作罢！


Thanks for reading :)
