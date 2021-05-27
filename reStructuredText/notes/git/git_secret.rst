.. meta::
    :robots: noindex

Git secret
==========

Begin with an existing or new git repository: ::

    $ git init

Initialize the *git-secret* repository: ::

    $ git secret init

Tell *git-secret* which gpg to use to encrypt file: ::

    $ git secret tell an9wer@gmail.com

Add files to encrypt: ::

    $ git secret add /path/to/file

Encrypt all files which have been added: ::

    $ git secret hide

Decrypt all encrypted files: ::

    $ git secret reveal

Show content of encrypted file: ::

    $ git secret cat /path/to/encrypted/file

