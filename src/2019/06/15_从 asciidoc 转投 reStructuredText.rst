从 asciidoc 转投 reStructuredText
=================================

大概在几个月前，我从 vimwiki 转投到了 asciidoc。先如今，我又从 asciidoc 转投到
了 reStructuredText。我可真是能够折腾，呵呵。

这次转投的原因是在于使用了一段时间 asciidoc 之后，愈发觉得其语法别扭，又或者说
是 reStructuredText 的语法更符合我的审美，加之 reStructuredText 似乎比 asciidoc
在文档圈里更为流行。当然，语法才是我选择 reStructuredText 的根本原因。

好在使用 docutils 库可以很容易地将 reStructuredText 文档转化成 html 格式，加之
之前写过针对 asciidoc 的 build 脚本，只需在其基础上进行修改即可。因此，我的转投
工作被大大地简化，大约使用了一个礼拜的时间完成。

另一点，这次也顺带更新了 notes 专栏。以前一直是拿 vimwiki 来记笔记的，这次转投
之后打算将所有笔记重新整理一遍，因为同时使用两种标记语言会有些绕脑子，所以这次
就打算让 reStructuredText 来一统天下。

当然，我唯一舍不得 vimwiki 的地方是它的链接跳转功能（在 url 或 path 文本上按下
回车即可进行跳转）。但是，我也找到了非常简单的替代方案：在 vim 中使用 gf 可以跳
转 path，使用 gx 可以跳转 url。同时，为了避免影响文本的内容，在
reStructuredText 中使用 comment 语法来定义这些跳转。这样我就可以放心地卸载
vimwiki 了。

现在我真的是爱上这套方案了。而且，最近我也突然意识到笔记的重要性，所谓好记性不
如烂笔头，所以平时遇到一些重要的东西，不管是某个软件的部署指令，还是某个命令的
使用教程，我都会打开 notes，将它们记录下来，方便以后的回顾。

Thanks for reading :)

