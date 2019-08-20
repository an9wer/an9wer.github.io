Nagios
======

Install nagios on CentOS7:

::

    # yum install epel-release
    # yum install nagios
    # yum install nagios-plugins-all

Start nagios service (disable selinux first):

::

    # setenforce 0
    # systemctl start nagios


Install httpd server which has nagios configuration by default, so we just
generate password of nagios user (*nagiosadmin* here), and put them to
*/etc/nagios* directory:

::

    # yum install httpd
    # htpasswd -c /etc/nagios/passwd nagiosadmin

**Note**: The authorized user is *nagiosadmin* here, which can be changed in
*/etc/nagios/cgi.cfg* file.
    

Start httpd service:

::

    # systemctl start httpd

Then visit *http://xxx.xxx.xxx.xxx/nagios*.

Nagios plugins
--------------

Nagios plugins directory: */usr/lib64/nagios/plugins*.


Nrpe
----

Install *check_nrpe* plugin on the monitoring machine:

::

    # yum install epel-release
    # yum install nagios-plugins-nrpe


Install and start *nrpe* daemon on the remote machine:

::

    # yum install epel-release
    # yum install nrpe
    # system start nrpe

Then, on the monitoring machine, run the following commmand to check remote
machine:

::

    # /usr/lib64/nagios/plugins/check_nrpe -H <remote host> -c <command>


References
----------

-   `NRPE document <https://assets.nagios.com/downloads/nagioscore/docs/nrpe/NRPE.pdf>`_

