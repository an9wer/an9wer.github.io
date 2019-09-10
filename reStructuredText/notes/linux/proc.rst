Linux proc
==========

Process file:

::

    $ ls -l /proc/<pid>/exec

Interrupts:

::

    $ less /proc/interrupts
    
Audio devices:

::

    $ cat /proc/asound/cards 


Speed of NIC:

::

    $ cat /sys/class/net/<interface>/speed
