.. meta::
    :robots: noindex

TigerVNC
========

VNC only can be used in GUI, instead of console.

Installation
------------

Install TigerVNC server on CentOS7:

::

    # yum install tigervnc-server

Install TigerVNC client on CentOS7:

::

    # yum install tigervnc

Server setup
------------

Run vncserver:

::

    $ vncserver

When vncserver is run with no options at all, it will choose the first
available display number (usually :1), start Xvnc with that display number, and
start the default window manager in the Xvnc session. It will also listen a
tcp port on number *5900 + display number*.

You can also specify the display number, in which case vncserver will attempt
to start Xvnc with that display number and exit if the display number is not
available:

::

    $ vncserver :{display}

The first time when vncserver is run, it will ask you to set password and
create *$HOME/.vnc* directory. You can modify password by using the following
command:

::

    $ vncpasswd {passwd-file}

Its default behavior is to prompt for a VNC password and then store an
obfuscated version of this password to passwd-file (or to *$HOME/.vnc/passwd*
if no password file is specified.)

**Note**: Only the first eight characters of VNC password are significant.

Editing the file *$HOME/.vnc/xstartup* allows you to change the applications run
at startup (but note that this will not affect an existing VNC session.)

::

    $ vim $HOME/.vnc/xstartup
        exec startxfce4
    $ vncserver :{display}

Or run a custom startup script:

::

    $ vncserver -xstartup "exec startxfce4" :{display}

To list all vnc servers:

::

    $ vncserver -list

To kill a vnc server:

::

    $ vncserver -kill :{display}

Another way is use *x0vncserver* which allows direct control over a physical X
session:

::

    $ x0vncserver -rfbauth ~/.vnc/passwd

**Note**: x0vncserver is an inefficient VNC server which continuously polls any
X display, allowing it to be controlled via VNC. It is intended mainly as a
demonstration of a simple VNC server. 


Client setup
------------

::

    $ vncviewer {ip}:{display}

Or:

::

    $ vncviewer {ip}::{port}

The port number is *5900 + display number* (e.g. 5901 if display number is 1).


References
----------

`ArchWiki: TigerVNC <https://wiki.archlinux.org/index.php/TigerVNC>`_

`VNC on linux <https://www.stuartellis.name/articles/vnc-on-linux/#manually-launching-vnc>`_

