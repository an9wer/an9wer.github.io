Contentsrv
==========

Download eflasher img:

::

    nanopi-m1-plus_eflasher_debian-jessie_4.14_armhf_20190522.img.zip

Flash it into micro SD card:

::

    dd if=/path/to/nanopi-m1-plus_eflasher_debian-jessie_4.14_armhf_20190522.img.zip of=/dev/sdX oflag=sync status=progress

Insert micro SD card into NanoPi M1 Plus, then follow tips to install.


After system installation, reboot to it, update system and install python3:

::

    $ sudo apt update
    $ sudo apt upgrate
    $ sudo apt install python3 python3-pip python3-venv python3-tk

Download project and change to project directory, then install Python
requirements:

::

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

**Note**: If error occurs when installing Pillow, you may install old version
of Pillow (i.e. `Pillow==5.4.1`).


Run client
----------

Uncomment related line in *config.ini* file.

::

    interval_seconds=15
    images_url=http://xxx.xxx.xxx.xxx:pppp/path/to/images

Create desktop:

::

    [Destop Entry]
    Type=Application
    Exec=/path/to/venv/bin/python /path/to/contentsrv/src/client.py
    Hidden=false
    NoDisplay=false
    X-GNOME-Autostart-enabled=true
    Name=image_client

*Note*: If need to start client automatically after booting system, you should
copy above *.desktop" file into `~/.config/autostart` directory.

