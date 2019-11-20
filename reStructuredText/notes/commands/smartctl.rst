smartctl
========

Print device info: ::

    # smartctl -i <device>

Print the vendor specific SMART attributes: ::

    # smartctl -A <device>

Print generic SMART capabilites, include an approximate indication of the time
duration of the various tests: ::

    # smartctl -c <device>

Run self-test: ::

    # smartctl -t short|long <device>

Run self-test in captive mode [ATA], or in Foreground mode [SCSI]: ::

    # smartctl -C -t short|long <device>

Abort non-captive SMART self-test: ::

    # smartctl -X <device>

To check result of self-test: ::

    # smartctl -l selftest <device>


References
----------

``man smartctl``

`Smart tests with smartctl
<https://www.thomas-krenn.com/en/wiki/SMART_tests_with_smartctl>`_
