Vagrant
=======

Commands
--------

Init *Vagrantfile*:

::

    $ vagrant init [<box name>]

Create and configure guest machine according *Vagrantfile* (See `How to define
a machine name in Vagrantfile <https://stackoverflow.com/a/20431791>`_) :

::

    $ vagrant up [<machine name>]

Shut down the running machine:

::

    $ vagrant halt [<machine name>]

Reload (halt and up) machine:

::

    $ vagrant reload [<machine name>]

Check the state of machine:

::

    $ vagrant status [<machine name>]


Runs any configured provisioners in *Vagrantfile*:

::

    $ vagrant provision [<machine name>]

Watch all local directories of any rsync synced folders and automatically
initiates an rsync transfer when changes are detected. (This command does not
exit until an interrupt is received.)

::

    $ vagrant rsync-auto


References
----------

`Vagrant documentation <https://www.vagrantup.com/docs/>`_
