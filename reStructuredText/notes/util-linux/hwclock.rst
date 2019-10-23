Hwclock
=======

Hardware clock
    Also known as the "RTC", "CMOS clock.  It's a battery driven clock which
    keeps track of time when the system is turned off.

    It keeps track of time when the system is turned off but is not used when
    the system is running.

    The hardware clock can be set from the BIOS setup screen or from whatever
    operating system is running.

System clock
    Sometimes called the "kernel clock" or "software clock") which is a
    software counter based on the timer interrupt. 

    It does not exist when the system is not running, so it has to be
    initialized from the RTC (or some other time source) at boot time. 

Diskplay current date and time from hardware clock: ::

    # hwclock

Set the hardware clock from the system clock: ::

    # hwclock -w

Set the system time from the hardware clock: ::

    # hwclock -s


References
----------

``man hwclock``

`The hardware and system clocks <http://tldp.org/HOWTO/Clock-2.html>`_
