ALSA
====

arecord & aplay
---------------

List devices:

::

    $ arecord -l

amixer
------

Show information of mixer devices:

::

    $ amixer info

Show a complete list of mixer controls:

::

    $ amixer scontrols

Show a complete list of mixer controls with contents:

::

    $ amixer scontents

Show content of a specified mixer control:

::

    $ amixer get <control>

    e.g.
    $ amixer get Master
    $ amixer get Headphone

Set content of a specified mixer control:

::

    $ amixer set <control> <parameter> [...]

    e.g.
    $ amixer set Master 5%+
    $ amixer set Master 30%
    $ amixer set Master 5dB-
    $ amixer set Master mute
    $ amixer set Master unmute


Reference
---------

``man arecord``

``man amixer``

`Arch wiki: ALSA <https://wiki.archlinux.org/index.php/Advanced_Linux_Sound_Architecture>`_

