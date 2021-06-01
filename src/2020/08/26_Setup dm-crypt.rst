Setup dm-crypt
==============

最近把自己的 NAS 组装起来了（有时间的话也另外写一篇 blog 来讲讲我是怎么组装这台
NAS 的），本来打算按照之前的方法直接上 raid1，但是这次又想让数据存储更加安全，
于是在 raid 上面再加了一层 dm-crypt。

Generage a keyfile: ::

    # dd if=/dev/urandom of=/path/to/<key file> bs=1 count=4096

Creating an encrypted storage: ::

    # cryptsetup -s 512 luksFormat /dev/<device> /path/to/<key file>

Open up the encrypted storage: ::

    # cryptsetup luksOpen -d /path/to/<key file> /dev/<device> <mapper name>

Format and mount the encrypted storage: ::

    # mkfs.ext4 /dev/mapper/<mapper name>
    # mount /dev/mapper/<mapper name> /mnt

Close the encrypted storage: ::

    # cryptsetup luksClose <mapper name>

Automate mounting the encrypted storege: ::

    # vim /etc/conf.d/dmcrypt
        target='crypt'
        source=UUID="<uuid>"
        key='/path/to/<key file>'
    # vim /etc/fstab
        UUID=<uuid> /mnt ext4 defaults 0 0

    # rc-update add dmcrypt boot

Thanks for reading :)

References
----------

`Gentoo wiki: dm-crypt
<https://wiki.gentoo.org/wiki/Dm-crypt>`_
