ftp
===


Login in ftp server in active mode: ::

    $ ftp -A <sever> <port>

Login in ftp server in passive mode: ::

    $ ftp -p <server> <port>

Commands
--------

cd <REMOTE-DIRECTORY>
    Change the working directory on the remote machine to <REMOTE-DIRECTORY>.

lcd <LOCAL-DIRECTORY>
    Change the working directory on the local machine. If no directory is
    specified, the user's home directory is used.

get|recv  <REMOTE-FILE> [<LOCAL-FILE>]
    Retrieve the REMOTE-FILE and store it on the local machine.  If a local
    file name is not specified, the local copy is given the same name as is
    stated for the remote original, subject to alteration by the current
    'case', 'ntrans', and 'nmap' settings.  The current settings for 'type',
    'form', 'mode', and 'structure' are effective during file transfer.

put|send  <LOCAL-FILE> [<REMOTE-FILE>]
    Store a local file on the remote machine. If REMOTE-FILE is left
    unspecified, the local file name is used after processing according to any
    'ntrans' or 'nmap' settings in naming the remote file.  File transfer uses
    the current settings for type, format, mode, and structure.


References
----------

``info ftp``
