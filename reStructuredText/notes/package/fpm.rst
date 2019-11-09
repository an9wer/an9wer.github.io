Fpm
===

Installation
------------

Install on CentOS 7: ::

    # yum install ruby-devel gcc make rpm-build rubygems
    # gem install --no-ri --no-rdoc fpm


Usage
-----

Create package from a single directory or multiple directories: ::

    $ fpm -s dir -t <target> -v <version> [--iteration <release>] -n <name> <directory> [<directory> ...]

Create pacakge from a single directory, and specify prefix of target: ::

    $ fpm -s dir -t <target> -v <version> [--iteration <release>] -n <name> --prefix <prefix> <directory>

