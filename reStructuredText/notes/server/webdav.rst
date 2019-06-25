WebDAV
======

Definition of WebDAV:

-   `Wikipedia: WebDAV <https://en.wikipedia.org/wiki/WebDAV>`_

Deploy WebDAV on CentOS 7:

Install httpd and creat realated directory:

::

    # yum install httpd
    # mkdir /var/www/webdav
    # chown -R apache:apache /var/www/webdav

Generate authentication file:

::

    htpasswd -c /etc/httpd/.passwd username

    
Confiure httpd configuration file (*/etc/httpd/conf.d/webdav.conf*),The
relevant lines are like this:

::

    DAVLockDB /var/lib/dav/DAVLock

    <VirtualHost *:80>
        Alias /webdav "/var/www/webdav"
        DocumentRoot /var/www/webdav
        <Directory "/var/www/webdav">
            DAV On
            AllowOverride None
            Options Indexes FollowSymLinks
            AuthType Basic
            AuthName "WebDAV"
            AuthUserFile /etc/httpd/.passwd
            Require valid-user
        </Directory>
    </VirtualHost>


**References**:

-   `Archwiki: WebDAV <https://wiki.archlinux.org/index.php/WebDAV>`_

-   `how-to-configure-webdav-access-with-apache-on-ubuntu-14-04 <https://www.digitalocean.com/community/tutorials/how-to-configure-webdav-access-with-apache-on-ubuntu-14-04>`_

-   `how-to-enable-webdav-on-apache-http-server-2-4-x <https://www.joe0.com/2019/01/25/how-to-enable-webdav-on-apache-http-server-2-4-x/>`_

-   `Configuring WebDAV on Apache server <https://www.ibm.com/support/knowledgecenter/en/SSEP7J_10.2.2/com.ibm.swg.ba.cognos.inst_cr_winux.10.2.2.doc/t_enablewebdavforreportstudio.html>`_

