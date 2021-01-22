Vim plugin
==========

See ``:h plugin``, ``:h initialization`` and ``:h runtimepath``

There are two types of plugins:

1. global plugin: Used for all kinds of files
2. filetype plugin: Only used for a specific type of file

Global plugin
-------------

You can see most global plugins in the directory *$VIMRUNTIME/plugin*.

Filetype plugin
---------------

See ``:h ftplugins``

A filetype plugin is like a global plugin, except that it sets options and
defines mappings for the current buffer only.

You can add a filetype plugin by dropping it in the right directory
(*$VIMRUNTIME/ftplugin*): ::

    ~/.vim/ftplugin/c.vim
    ~/.vim/ftplugin/c_another.vim
    ~/.vim/ftplugin/python.vim
