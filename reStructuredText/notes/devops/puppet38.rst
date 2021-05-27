.. meta::
    :robots: noindex

Puppet3.8
=========

Puppet is **declarative**, **idempotent**, and **stateless** by default.

Installation
------------

Install puppet3.8 on CentOS7: ::

    # rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
    # yum install puppet

https://puppet.com/docs/puppet/3.8/install_el.html

Install puppet 5.5 on CentOS8: ::

    # rpm -ivh https://yum.puppetlabs.com/puppet5-release-el-8.noarch.rpm
    # dnf install puppet-agent
    # dnf install puppetserver

https://www.theskillpedia.com/setup-puppet-master-and-puppet-agent-on-centos-8/

Install puppet 5.5 on CentOS7: ::

    # rpm -Uvh https://yum.puppet.com/puppet5-release-el-7.noarch.rpm
    # yum install puppet-agent
    # yum install puppetserver

    # /opt/puppetlabs/bin/puppet resource service puppet ensure=running enable=true

    [main]
    certname = agent5
    server = puppet-master
    environment = production
    runinterval = 1h

    # /opt/puppetlabs/bin/puppet agent --test


Install puppet 5.5 on CentOS6: ::

    # rpm -Uvh https://yum.puppet.com/puppet5-release-el-6.noarch.rpm
    # yum install puppet-agent
    # yum install puppetserver



Subcommands
-----------

module
""""""

Install a module:

::

    # puppet module install <module>

Install a specified version of module:

::

    # puppet module install -v <version> <module>


apply
"""""

Dry run:

::

    # puppet apply --noop <foo.pp>

Resource
--------

Exec
""""

refreshonly
    When this attribute is set to *true*, the command will be triggered by
    resources it subscribes (by using *subscribe* or *notify* attribute, not
    *require* or *before*).

    ::

        exec { "some command":
            refreshonly => only,
            require => File['some file'],
        }

    In this example, whether the required *file* resource is run, the *exec*
    resource will never be triggered.


References
----------

https://elatov.github.io/2014/09/writing-better-puppet-modules/
