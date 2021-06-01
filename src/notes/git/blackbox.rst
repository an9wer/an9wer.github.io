.. meta::
    :robots: noindex

Blackbox
========

Install blackbox: ::

    $ git clone https://github.com/StackExchange/blackbox.git
    $ cd blackbox
    $ sudo make symlinks-install

Init blackbox in a git repository: ::

    $ blackbox_initialize
    $ git add .blackbox/.gitattributes
    $ git commit -m'INITIALIZE BLACKBOX' .blackbox .gitignore


Add gpg key to admin: ::

    $ blackbox_addadmin <keyname>

Register a file (encrypt and commit): ::

    $ blackbox_register_new_file <file>

View a encrypted file: ::

    $ blackbox_view <file.gpg>


Edit a encrypted file (decrypt it first and encrypt it after editing): ::

    $ blackbox_edit <file.gpg>

List all registered files:: 

    $ blackbox_list_files

Remove a registered file: ::

    $ blackbox_deregister_file <file>

References
----------

`Github repository of blackbox
<https://github.com/StackExchange/blackbox>`_

