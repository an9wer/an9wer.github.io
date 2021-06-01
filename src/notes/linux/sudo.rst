.. meta::
    :robots: noindex

Linux sudo
==========

The sudoers file grammar will be described below in Extended Backus-Naur Form
(EBNF): ::

    User_Spec ::= User_List Host_List '=' Cmnd_Spec_List \
                  (':' Host_List '=' Cmnd_Spec_List)*

    User_List ::= User |
                  User ',' User_List

    Host_List ::= Host |
                  Host ',' Host_List

    Cmnd_Spec_List ::= Cmnd_Spec |
                       Cmnd_Spec ',' Cmnd_Spec_List
                       
User: ::

    User ::= '!'* user name |
             '!'* #uid |
             '!'* %group |
             '!'* %#gid |
             '!'* +netgroup |
             '!'* %:nonunix_group |
             '!'* %:#nonunix_gid |
             '!'* User_Alias

    User_Alias ::= NAME '=' User_List
             
Host: ::

    Host ::= '!'* host name |
             '!'* ip_addr |
             '!'* network(/netmask)? |
             '!'* +netgroup |
             '!'* Host_Alias

    Host_Alias ::= NAME '=' Host_List


Cmnd_Spec_List: ::

    Cmnd_Spec_List ::= Cmnd_Spec |
                       Cmnd_Spec ',' Cmnd_Spec_List

    Cmnd_Spec ::= Runas_Spec? SELinux_Spec? Solaris_Priv_Spec? Tag_Spec* Cmnd

    Runas_Spec ::= '(' Runas_List? (':' Runas_List)? ')'

    SELinux_Spec ::= ('ROLE=role' | 'TYPE=type')

    Solaris_Priv_Spec ::= ('PRIVS=privset' | 'LIMITPRIVS=privset')

    Tag_Spec ::= ('EXEC:' | 'NOEXEC:' | 'FOLLOW:' | 'NOFOLLOW' |
                  'LOG_INPUT:' | 'NOLOG_INPUT:' | 'LOG_OUTPUT:' |
                  'NOLOG_OUTPUT:' | 'MAIL:' | 'NOMAIL:' | 'PASSWD:' |
                  'NOPASSWD:' | 'SETENV:' | 'NOSETENV:')

Runas_List: ::

    Runas_List ::= Runas_Member |
                   Runas_Member ',' Runas_List

    Runas_Member ::= '!'* user name |
                     '!'* #uid |
                     '!'* %group |
                     '!'* %#gid |
                     '!'* %:nonunix_group |
                     '!'* %:#nonunix_gid |
                     '!'* +netgroup |
                     '!'* Runas_Alias

    Runas_Alias ::= NAME '=' Runas_List


Cmnd: ::

    Cmnd ::= Digest_Spec? '!'* command name |
             '!'* directory |
             '!'* "sudoedit" |
             '!'* Cmnd_Alias

    Cmnd_Alias ::= NAME '=' Cmnd_List

    Cmnd_List ::= Cmnd |
                  Cmnd ',' Cmnd_List

Reserved word ALL
-----------------

The reserved word *ALL* is a built-in alias that always causes a match to
succeed. It can be used wherever one might otherwise use a *Cmnd_Alias*,
*User_Alias*, *Runas_Alias*, or *Host_Alias*.


The includedir directive
------------------------

The #includedir directive can be used to create a sudoers.d directory that the
system package manager can drop sudoers file rules into as part of package
installation. For example, given: ::

    #includedir /etc/sudoers.d

sudo will read each file in /etc/sudoers.d, skipping file names that end in '~'
or contain a '.' character to avoid causing problems with package manager or
editor temporary/backup files. Files are parsed in sorted lexical order. That
is, /etc/sudoers.d/01_first will be parsed before /etc/sudoers.d/10_second. Be
aware that because the sorting is lexical, not numeric, /etc/sudoers.d/1_whoops
would be loaded after /etc/sudoers.d/10_second. Using a consistent number of
leading zeroes in the file names can be used to avoid such problems.


References
----------

``man sudoers``
