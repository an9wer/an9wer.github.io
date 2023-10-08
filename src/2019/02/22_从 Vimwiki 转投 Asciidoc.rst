从 Vimwiki 转投 Asciidoc
========================

:Published: 2019/02/22

.. meta:
    :tags: review

从这个博客搭建至今，我一直使用 vimwiki 来记录我的博文。但是用久了之后发现
vimwiki 的几个痛点：

1.  某些特殊字符无法进行转义，如 $。
2.  List 中嵌套 Preformatted text 会比较麻烦。
3.  大文件 build 成 HTML 会比较慢。
4.  不支持批量文件 build。

因此我就有了寻找更合适的标记语言来替换 vimwiki 的想法，以解决上面提到的痛点。

本来想回到 Markdown 阵营，打算用 CommonMark，结果发现它不支持 table，于是我又打
了退堂鼓。

继而我又找到了 reStructuredText，Asciidoc （关于他们和 Markdown 的比较可以看
`这篇文章 <https://www.ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/>`_
）。二者语法其实都大同小异，要论扩展性和流行度的话应该是前者比较好，但是最终我
选择了后者，因为 Asciidoc 文档更清晰，代码更简洁，且其代码托管在 Github 上，同
时更新也较为频繁。

之后就是将之前所有的博文转化成 Asciidoc 格式，这大概陆陆续续花了我半个月的时间
，现在也已基本完工，同时我也写了个 `脚本
<https://github.com/an9wer/an9wer.github.io/blob/master/asciidoc/build>`_ ，方
便将新建或者修改的 Asciidoc 文件重新 Build 成 HTML5 文件。

Thanks for reading :)

