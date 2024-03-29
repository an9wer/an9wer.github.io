用 RSS 订阅网站的更新
=====================

:Published: 2018/12/08

.. meta::
    :tags: misc
    :description: 尝试使用 innoreader 来订阅一些博客、新闻网站等，把内容聚合在
        一个统一的平台上，定期获取新的资讯。

在这之前，我对 RSS 这东西的认知属于听名字很熟，但不知道具体是什么的范畴。但因为
开始写博客，而大多数的博客网站都有 RSS 订阅功能，于是出于好奇，最近也就研究了一
下，发现还真是个好东西。以下属于我自己的理解：

    RSS 定义了一套标准，其使用 xml 格式，并且规定了一系列的元素，只要发布者和接
    受者都遵循这个规则，就可以分别实现内容的发布与订阅。


利用 RSS 订阅这个功能，可以将不同网站资讯汇集到一个平台进行统一浏览，这样可以大
大地提高获取资讯的效率。像我的话平时会关注电子产品，Linux，新闻等方面的资讯，而
这些网站大部分都支持 RSS 订阅，所以我在手机上下载了一个名为 `Inoreader
<https://www.inoreader.com/>`_ 的应用，用来订阅这些网站的资讯，这样就不用每次都
逐个地打开各个网站来获取资讯了。

当然也有些网站不支持 RSS 订阅功能，那我们该怎么办呢？其实也很简单，我们可以自己
写一个脚本，爬取网站的资讯，然后生成 RSS 规范的 xml 文件，最后将 xml 文件放在静
态文件服务器上，并将该地址添加到 RSS 阅读软件中（例如上面提到的 Inoreader），我
们就可以获取这些网站的资讯了。

目前我在使用中确实发现有些网站不支持 RSS 订阅功能，例如简书等，本来想自己写个脚
本的，但我发现了一个名为 `RSSHub <https://github.com/DIYgod/RSSHub>`_ 项目，这
个项目中就已经包含了我想要的一些网站的 RSS 订阅功能的生成，所以我为了省事，就直
接拿来用了。当然之后如果有其它需求，应该还会自己写个，毕竟我还是喜欢用自己写的
东西，虽然 bug 可能会比较多，但我能掌控一切，呵呵！

Updated 2021/01/20
------------------

时隔两年终于为我这个博客平台添加了 `RSS 订阅地址 </blog.xml>`_ ，欢迎各位订阅。

Thanks for reading :)
