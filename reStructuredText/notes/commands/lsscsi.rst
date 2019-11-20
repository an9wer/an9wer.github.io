lsscsi
======

The transports that are currently recognized are: IEEE 1394, ATA, FC, iSCSI,
SAS, SATA, SPI, SRP and USB.


To list classic information: ::

    $ lsscsi -c

Or: ::

    $ cat /proc/scsi/scsi

To list transport information: ::

    $ lsscsi -t

References
----------

`SCSI Interfaces Guide
<https://www.kernel.org/doc/html/v4.17/driver-api/scsi.html>`_

`Wikipedia: scsi <https://en.wikipedia.org/wiki/SCSI>`_
    SCSI is most commonly used for hard disk drives and tape drives, but it can
    connect a wide range of other devices, including scanners and CD drives,
    although not all controllers can handle all devices.

    SCSI, a parallel intgerface, is derived from SASI, and was gradually
    replaced by SAS (Serial Attached SCSI) since 2005.
    
`How SCSI Works <https://computer.howstuffworks.com/scsi.htm>`_

`What’s The Difference Between SATA And SAS Hard Drives?  <https://www.pickaweb.co.uk/kb/difference-between-sata-sas-hard-drives/>`_
    SAS drives tend to be used for Enterprise Computing where high speed and
    high availability are crucial such as banking transactions and Ecommerce.

    SATA drives tend to be used for desktops, consumer use and for less
    demanding roles such as data storage and backups.

    SAS drives are more reliable than SATA drives. 

`Understanding SAS, SATA, SCSI and ATA <https://www.webopedia.com/DidYouKnow/Computer_Science/sas_sata.asp>`_
    SCSI, short for small computer system interface, is a parallel interface
    standard used by Apple Macintosh computers, PCs and many UNIX systems for
    attaching peripheral devices to computers.

    Serial Attached SCSI, abbreviated as SAS, an evolution of parallel SCSI
    into a point-to-point serial peripheral interface in which controllers are
    linked directly to disk drives.

    ATA, also known as IDE, is a disk drive implementation that integrates the
    controller on the disk drive itself. 

    Serial ATA, Often abbreviated as SATA, is an evolution of the Parallel ATA
    physical storage interface. 

`Why do my SATA devices show up under /proc/scsi
<https://unix.stackexchange.com/questions/3901/why-do-my-sata-devices-show-up-under-proc-scsi-scsi>`_

`In what sense does SATA “talk” SCSI? How much is shared between SCSI and ATA?
<https://unix.stackexchange.com/questions/144561/in-what-sense-does-sata-talk-scsi-how-much-is-shared-between-scsi-and-ata>`_
