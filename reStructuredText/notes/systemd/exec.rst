Systemd exec
============

EnvironmentFile
    Similar to Environment= but reads the environment variables from a text
    file.

    The argument passed should be an absolute filename or wildcard expression,
    optionally prefixed with "-", which indicates that if the file does not
    exist, it will not be read and no error or warning message is logged.

    Example: ::

        # cat /usr/lib/systemd/system/ntpd.service
        [Unit]
        Description=Network Time Service
        After=syslog.target ntpdate.service sntp.service

        [Service]
        Type=forking
        EnvironmentFile=-/etc/sysconfig/ntpd
        ExecStart=/usr/sbin/ntpd -u ntp:ntp $OPTIONS
        PrivateTmp=true

        [Install]
        WantedBy=multi-user.target

