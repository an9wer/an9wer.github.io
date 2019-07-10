..
    Commands
        ./notes/commands/info.rst
        ./notes/commands/top.rst
        ./notes/commands/pstree.rst
        ./notes/commands/dmidecode.rst
        ./notes/commands/ntp.rst
        ./notes/commands/sed.rst
    Coreutils
        ./notes/coreutils/mktemp.rst
    Package
        ./notes/package/rpm.rst
        ./notes/package/yum.rst
        ./notes/package/fpm.rst
    Git
        ./notes/git/git_secret.rst
    Bash
        ./notes/bash/variables.rst
        ./notes/bash/expansion.rst
    Vim
        ./notes/vim/tricks.rst
        ./notes/vim/options.rst
        ./notes/vim/pattern.rst
        ./notes/vim/window.rst
        ./notes/vim/tabpage.rst
        ./notes/vim/repeat.rst
        ./notes/vim/various.rst
        ./notes/vim/netrw.rst
    DevOps
        ./notes/devops/puppet38.rst
    Storage
        ./notes/storage/glusterfs.rst
    Database
        ./notes/database/redis.rst
    Hardware
        ./notes/hardware/memory.rst
    Server
        ./notes/server/httpd.rst
        ./notes/server/webdav.rst
        ./notes/server/tigervnc.rst
    Awesome
        ./notes/awesome/redshift.rst
    Misc
        ./notes/miscellaneous/programming_language.rst
        ./notes/miscellaneous/operating_system.rst
        ./notes/miscellaneous/desktop_environment.rst
        ./notes/miscellaneous/hardware.rst
        ./notes/miscellaneous/regex.rst
    NS
        ./notes/ns/contentsrv.rst
    TODO
        ./notes/coreutils/seq.rst

        https://wiki.archlinux.org/index.php/XScreenSaver
        https://wiki.archlinux.org/index.php/Backlight
        https://wiki.archlinux.org/index.php/Display_Power_Management_Signaling
        https://www.jwz.org/xscreensaver/man1.html

        puppet: inherit and include
        puppet: default resource
        puppet: contain

        bash: $_

Commands/
    `info </notes/commands/info.html>`_

    `top </notes/commands/top.html>`_

    `pstree </notes/commands/pstree.html>`_

    `dmidecode </notes/commands/dmidecode.html>`_

    `ntp </notes/commands/ntp.html>`_

    `sed </notes/commands/sed.html>`_

Coreutils/
    `mktemp </notes/coreutils/mktemp.html>`_

Package/
    `RPM </notes/package/rpm.html>`_

    `fpm <notes/package/fpm.html>`_

Bash/
    `variables </notes/bash/variables.html>`_

    `expansion </notes/bash/expansion.html>`_

Vim/
    `tricks </notes/vim/tricks.html>`_

    `options </notes/vim/options.html>`_

    `pattern </notes/vim/pattern.html>`_

    `window </notes/vim/window.html>`_

    `tabage </notes/vim/tabpage.html>`_

    `repeat </notes/vim/repeat.html>`_

    `various </notes/vim/various.html>`_

    `netrw </notes/vim/netrw.html>`_ 

Git/
    `git secret </notes/git/git_secret.html>`_

DevOps/
    `puppet3.8 </notes/devops/puppet38.html>`_

Storage/
    `glusterfs </notes/storage/glusterfs.html>`_

Database/
    `redis </notes/database/redis.html>`_

Hardware/
    `memory </notes/hardware/memory.html>`_

Server/
    `httpd </notes/server/httpd.html>`_

    `WebDAV </notes/server/webdav.html>`_

    `TigerVNC </notes/server/tigervnc.html>`_

Awesome/
    `redshift </notes/awesome/redshift.html>`_

Misc/
    `Programming language </notes/miscellaneous/programming_language.html>`_

    `Operating system </notes/miscellaneous/operating_system.html>`_

    `Hardware </notes/miscellaneous/hardware.html>`_

    `regex </notes/miscellaneous/regex.html>`_


HowTo
-----

Q : How to check CentOS version?

A1:
    ::

        $ rpm -q centos-release

A2:
    ::

        $ cat /etc/centos-release

----

Q : How to apply a free doman name?

A : `freenom <https://www.freenom.com/>`_

----

Q : How to find my public ip address?

A1:
    ::

        $ dig +short myip.opendns.com @resolver1.opendns.com

A2:
    ::

        $ dig TXT +short o-o.myaddr.l.google.com @ns1.google.com

A3:
    ::

        $ curl ifconfig.me

R :
    `How to find my public ip address from command line?
    <https://www.cyberciti.biz/faq/how-to-find-my-public-ip-address-from-command-line-on-a-linux/>`_

    `What is 'myip.opendns.com' doing?  <https://unix.stackexchange.com/a/335403>`_

----

Q : How to trim leading and trailing white space from a string in Bash?

A :
    ::

        $ echo " some string  " | xarg
        some string

R :
    `How to trim whitespace from a Bash variable? <https://stackoverflow.com/a/12973694>`_

