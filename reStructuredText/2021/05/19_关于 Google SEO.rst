关于 Google SEO
===============

:Published: : 2021/05/19

.. meta::
    :description: 现在这个网站也存在快 3 年了，但访问数量实在是少的可怜。之前不
        太在乎这些，因为很多文章是写给自己看的（也算是另一种笔记的形式），所以
        就只满足于孤芳自赏。但最近想法改变了，既然是公开的文章，也想看看自己写
        的文章能不能给别人提供些许帮助或者思路。所以打算学习下 Google SEO 的相
        关知识，想着把这个网站做起来，起码能有些流量。

现在这个网站也存在快 3 年了，但访问数量实在是少的可怜。之前不太在乎这些，因为很
多文章是写给自己看的（也算是另一种笔记的形式），所以就只满足于孤芳自赏。但最近
想法改变了，既然是公开的文章，也想看看自己写的文章能不能给别人提供些许思路或者
帮助。所以打算尝试下 Google SEO ，想着把这个网站做起来，起码能有些流量。

更新 URL
--------

遇到 url 变更的时候，例如，有时之前的博文更新后，url 也发生了改变，需要让旧的
url 从 google search index 中删除怎么办？

通常来说只要 google crawler 下次请求旧的 url 时得到 404 的返回结果，google 会自
动将旧的 url 从其 index 中删除，但是这样会有个时间差，即在 google crawler 来之
前，旧的 url 仍然会出现在 google search 的搜索结果中。如果我们不想这么被动的话
，可以先在 Removal tool 中手动提交一个临时删除 url 的请求给 google： ::

    Google Search Console -> Removals -> Temporary removals -> New request

提交后，会得到一条删除 url 的记录，如果其状态是 Processing request，说明 google
正在处理我们的删除请求，等到这个状态变成 Temporarily removed 之后，我们再通过
google 搜索相关关键字验证，这回发现结果中没有了旧的 url。

但不要高兴得太早，上面的方法只是把旧的 url 从 google 搜索结果中临时删除了，其还
保留在 google search index 中（google crawler 依然会继续爬取旧的 url），且有效
期只有 6 个月。也就是接下来不告诉 google crawler 要永久删除这个 url 的话（也就
是将 url 从 google serach index 中移除）， 等有效期过了之后，旧的 url 又会出现
在搜索结果中。那么如何永久删除旧的 url 呢？有三种方法：

1. 移除旧的 url 页面，即返回 404 或者 401 结果。
2. 给旧的 url 页面加上密码才能访问。
3. 在旧的 url 页面中加上 noindex meta tag。

**注意** ： 只有在我们给 google 手动提交临时删除旧的 url 请求，且要等到请求
状态变成 Temporarily removed 之后（在这个过程中旧的 url 必须依然要能被访问到，
不能是 404 等异常状态）。我们接下来才能使用上面的方法永久删除旧的 url。

    If your URL is unreachable by Google (404, 502/3) when you use this tool,
    it will assume that the page is gone, and your block request will expire.
    Any page found at that URL at a later time will be considered a new page
    that can appear in Google Search results.

另外，google 还提供了另外一种删除 url 的入口： Remove Outdated Content tool ::

    Google Search Console -> Removals -> Outdated Content

它和 temporary removals 的区别在于，如果你不是网站的所有者，想删除 url 请使用前
者提交删除申请，如果你是网站的所有者，请使用后者。

Thanks for reading :)
