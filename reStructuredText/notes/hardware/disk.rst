Hardware disk
=============

Physcial block size and logical block size
------------------------------------------

The logical block size is the size of the blocks that the UNIX kernel uses to
read or write files. The logical block size is usually different from the
physical block size (usually 512 bytes), which is the size of the smallest
block that the disk controller can read or write.

To check physcial and logical block size: ::

    Way 1
    # cat /sys/block/<device>/queue/physical_block_size 
    # cat /sys/block/<device>/queue/logical_block_size 

    Way 2
    # blockdev --getss <device>
    # blockdev --getpbsz /dev/sda 

    Way 3
    # smartctl -i <device>

    Way 4
    # hdparm -I <device>

`Archwiki: Advanced format
<https://wiki.archlinux.org/index.php/Advanced_Format#Aligning_Partitions>`_

`Wikipedia: Advanced format
<https://en.wikipedia.org/wiki/Advanced_Format>`_

`Thomas-krenn wiki: Advanced Sector Format of Block Devices
<https://www.thomas-krenn.com/en/wiki/Advanced_Sector_Format_of_Block_Devices>`_

`Logical block size
<https://docs.oracle.com/cd/E19455-01/805-7228/fsfilesysappx-9/index.html>`_


ATA, SATA, SCSI and SAS
-----------------------

`lsscsi
</notes/commands/lsscsi.html>`_


Disk enclosure
--------------

`Wikipedia: Disk Enclosure
<https://en.wikipedia.org/wiki/Disk_enclosure>`_


S.M.A.R.T
---------

`Wikipedia: S.M.A.R.T
<https://en.wikipedia.org/wiki/S.M.A.R.T.>`_


SSD
---

http://codecapsule.com/2014/02/12/coding-for-ssds-part-1-introduction-and-table-of-contents/

    Cells are grouped into a grid, called a **block**, and blocks are grouped
    into planes. The smallest unit through which a block can be read or written
    is a **page**. Pages cannot be erased individually, only whole blocks can
    be erased. The size of a NAND-flash page size can vary, and most drive
    have pages of size 2 KB, 4 KB, 8 KB or 16 KB. Most SSDs have blocks of 128
    or 256 pages, which means that the size of a block can vary between 256 KB
    and 4 MB. For example, the Samsung SSD 840 EVO has blocks of size 2048 KB,
    and each block contains 256 pages of 8 KB each. The way pages and blocks
    can be accessed is covered in details in Section 3.1.

    It is not possible to read less than one page at once. One can of course
    only request just one byte from the operating system, but a full page will
    be retrieved in the SSD, forcing a lot more data to be read than necessary.

    When writing to an SSD, writes happen by increments of the page size. So
    even if a write operation affects only one byte, a whole page will be
    written anyway. 

    A NAND-flash page can be written to only if it is in the “free” state. When
    data is changed, the content of the page is copied into an internal
    register, the data is updated, and the new version is stored in a “free”
    page, an operation called “read-modify-write”.

    Pages cannot be overwritten, and once they become stale, the only way to
    make them free again is to erase them. However, it is not possible to erase
    individual pages, and it is only possible to erase whole blocks at once. 
