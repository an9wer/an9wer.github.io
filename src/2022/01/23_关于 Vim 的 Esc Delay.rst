关于 Vim 的 Esc Delay
=====================

:Published: 2022/01/23

.. meta::
    :description: Vim 用户可能会遇到这种情况：
        莫名其妙地，在 command mode 或者 insert mode 中，
        按下 Esc 键后，会有个短暂的 delay，才能进入 normal model 中。
        虽然短暂，但是足以让人抓狂。

Vim 用户可能会遇到这种情况：
莫名其妙地，在 command mode 或者 insert mode 中，
按下 Esc 键后，会有个短暂的 delay，才能进入 normal model 中。
虽然短暂，但是足以让人抓狂。

所以，为何会出现 esc delay 呢？

有两种情况会在按下 Esc 键的时候发生 delay [#]_ ：

1. mapping delay: 使用 map 命令定义的 key 中包含了 Esc 键的 terminal code ``^[``
2. keycode delay: 某些键的 terminal code 含有 Esc 键的 terminal code ``^[`` ，例如 F5 的 terminal code ``^[[15~`` ；
   或者自己重新定义了某个键的 terminal code，例如 ``set <M-b>=^[b``

那么，怎样才能避免 esc delay 呢？

1. 如果是 mapping delay 导致的问题，则可以设置一个较短的 timeoutlen [#]_ ，例如 ``set timeoutlen=50``
2. 如果是 keycode delay 导致的问题，则可以设置一个较短的 ttimeoutlen [#]_ ，例如 ``set ttimeoutlen=50``

References
----------

.. [#] `Esc Delay <https://vi.stackexchange.com/a/20220>`_
.. [#] ``:h timeoutlen``
.. [#] ``:h ttimeoutlen``
