.. meta::
    :robots: noindex

xinit
=====

xinitrc
-------

To determine the client to run, startx looks for the following files, in
order: ::

    1. $(HOME)/.startxrc
    2. /usr/lib64/sys.startxrc
    3. $(HOME)/.xinitrc
    4. /etc/X11/xinit/xinitrc

xprofile
--------

An xprofile file, *~/.xprofile* and */etc/xprofile*, allows you to execute
commands at the beginning of the X user session - before the window manager is
started.

The xprofile files are natively sourced by the following display managers:
-   GDM - /etc/gdm/Xsession
-   LightDM - /etc/lightdm/Xsession
-   LXDM - /etc/lxdm/Xsession
-   SDDM - /usr/share/sddm/scripts/Xsession

It is possible to source xprofile from a session started from xinit or startx: ::

    #!/bin/sh

    # Make sure this is before the 'exec' command or it won't be sourced.
    [ -f /etc/xprofile ] && . /etc/xprofile
    [ -f ~/.xprofile ] && . ~/.xprofile

References
----------

``man startx``

`archwiki: xprofile
<https://wiki.archlinux.org/index.php/Xprofile>`_
