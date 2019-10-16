Commands/
    `ledger     </notes/commands/ledger.html>`_

    `info       </notes/commands/info.html>`_

    `top        </notes/commands/top.html>`_

    `iptables   </notes/commands/iptables.html>`_

    `ntp        </notes/commands/ntp.html>`_

    `sed        </notes/commands/sed.html>`_

    `dmidecode  </notes/commands/dmidecode.html>`_

    `lsscsi     </notes/commands/lsscsi.html>`_

    `xclip      </notes/commands/xclip.html>`_

    `xmodmap    </notes/commands/xmodmap.html>`_

    `fio        </notes/commands/fio.html>`_

    `bc         </notes/commands/fio.html>`_

    `ssh        </notes/commands/ssh.html>`_

    `lsof       </notes/commands/lsof.html>`_

Coreutils/
    `mktemp     </notes/coreutils/mktemp.html>`_

    `cut        </notes/coreutils/cut.html>`_

Psmisc/
    `pstree     </notes/psmisc/pstree.html>`_

Linux/
    `Linux filesystem hierarchy </notes/linux/filesystem_hierarchy.html>`_

    `Linux network </notes/linux/network.html>`_

    `Linux wireless </notes/linux/wireless.html>`_

    `Linux process </notes/linux/process.html>`_

    `Linux permissions </notes/linux/permissions.html>`_

    `Linux proc     </notes/linux/proc.html>`_

    `Linux sys      </notes/linux/sys.html>`_

    `Linux SELinux  </notes/linux/selinux.html>`_

    `Linux Systemd  </notes/linux/systemd.html>`_

    `Linux ALSA     </notes/linux/alsa.html>`_

    `Linux kickstart </notes/linux/kickstart.html>`_

    `Linux NetworkManager </notes/linux/networkmanager.html>`_

    `Linux memtest86+   </notes/linux/memtest86+.html>`_

Package/
    `RPM        </notes/package/rpm.html>`_

    `yum        </notes/package/yum.html>`_

    `dnf        </notes/package/dnf.html>`_

    `dpkg       </notes/package/dpkg.html>`_

    `apt        </notes/package/apt.html>`_

    `pacman     </notes/pacman/pacman.html>`_

    `fpm        <notes/package/fpm.html>`_

Bash/
    `Bash grammar    </notes/bash/grammar.html>`_

    `Bash quoting    </notes/bash/quoting.html>`_

    `Bash parameters </notes/bash/parameters.html>`_

    `Bash expansion  </notes/bash/expansion.html>`_

    `Bash redirection </notes/bash/redirection.html>`_

    `Bash builtin    </notes/bash/builtin.html>`_

    `Bash function   </notes/bash/function.html>`_

Vim/
    `Vim tricks     </notes/vim/tricks.html>`_

    `Vim options    </notes/vim/options.html>`_

    `Vim pattern    </notes/vim/pattern.html>`_

    `Vim editing    </notes/vim/editing.html>`_

    `Vim window     </notes/vim/window.html>`_

    `Vim tabage     </notes/vim/tabpage.html>`_

    `Vim repeat     </notes/vim/repeat.html>`_

    `Vim various    </notes/vim/various.html>`_

    `Vim quickfix   </notes/vim/quickfix.html>`_

    `Vim map        </notes/vim/map.html>`_

    `Vim netrw      </notes/vim/netrw.html>`_ 

Git/
    `git secret </notes/git/git_secret.html>`_

    `blackbox   </notes/git/blackbox.html>`_

Storage/
    `glusterfs  </notes/storage/glusterfs.html>`_

    `lvm        </notes/storage/lvm.html>`_

Database/
    `redis      </notes/database/redis.html>`_

Server/
    `nginx      <notes/server/nginx.html>`_

    `httpd      </notes/server/httpd.html>`_

    `WebDAV     </notes/server/webdav.html>`_

    `TigerVNC   </notes/server/tigervnc.html>`_

    `Nagios     </notes/server/nagios.html>`_

DevOps/
    `puppet3.8  </notes/devops/puppet38.html>`_

    `docker     </notes/devops/docker.html>`_

    `vagrant    </notes/devops/vagrant.html>`_

Language/
    `Java       </notes/language/java.html>`_

    `EBNF       </notes/language/ebnf.html>`_

    `Graphviz   </notes/language/grammar.html>`_

Awesome/
    `redshift   </notes/awesome/redshift.html>`_

Misc/
    `Programming language </notes/miscellaneous/programming_language.html>`_

    `Operating system </notes/miscellaneous/operating_system.html>`_

    `Hardware   </notes/miscellaneous/hardware.html>`_

    `Desktop environment </notes/miscellaneous/desktop_environment.html>`_

    `regex      </notes/miscellaneous/regex.html>`_

    `TLS/SSL    </notes/miscellaneous/tls_ssl.html>`_


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

----

Q : How to get TX/RX ?

A1:
    ::

        $ cat /proc/net/dev

A2:
    ::

        $ ip -s link
        
A3:
    ::

        $ netstat -i

R :
    `How to get TX/RX bytes without ifconfig? <https://serverfault.com/questions/533513/how-to-get-tx-rx-bytes-without-ifconfig>`_

----

Q : How to set default web browser in X11?

A :
    ::

        $ xdg-settings set default-web-browser <firefox.desktop|chromium.desktop>

R :
    `Archwiki: xdg-utils <https://wiki.archlinux.org/index.php/Xdg-utils>`_

----

Q : How to reset lost password in Linux?

R :
    `Archwiki: reset lost root password <https://wiki.archlinux.org/index.php/Reset_lost_root_password>`_

----

Q : How to Check if Your Computer Uses UEFI or BIOS?

A :
    The easiest way to find out if you are running UEFI or BIOS is to look for
    a folder */sys/firmware/efi*. The folder will be missing if your system is
    using BIOS.
