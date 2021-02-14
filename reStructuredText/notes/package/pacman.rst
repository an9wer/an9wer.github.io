Pacman
======

Handling config files
---------------------

See ``man 8 pacman /HANDLING CONFIG FILES``

During an upgrade, three MD5 hashes are used for each backup file to determine
the required action:

original=X, current=X, new=X
    Install the new file.

original=X, current=X, new=Y
    Install the new file.

original=X, current=Y, new=X
    Leave the current file in place.

original=X, current=Y, new=Y
    Install the new file.

original=X, current=Y, new=Z
    Install the new file with a .pacnew extension and warn the user. The user
    must then manually merge any necessary changes into the original file.

original=NULL, current=Y, new=Z
    Install the new file with a .pacnew extension and warn the user. The user
    must then manually merge any necessary changes into the original file.

Related files
-------------

/var/lib/pacman/local/package-version/files
    Contains metadata about this package. If this file gets corrupted, is empty
    or goes missing, it results in file exists in filesystem errors when trying
    to update the package.

S
-

Fix "Failed to commit transaction (conflicting files)" error: ::

    # pacman -S --overwrite <path> <pacakge>


Display information of remote packages: ::

    $ pacman -Si <package> [...]

Q
-

Query the package database. This operation allows you to view **installed**
packages and their files, as well as meta-information about individual packages
(dependencies, conflicts, install date, build date, size).

Q examples
""""""""""

Display owners of files (path): ::

    $ pacman -Qo <file> [...]

Display information (e.g. depends) of packages by query database: ::

    $ pacman -Qi <package> [...]

List all files owned by packages by query database: ::

    $ pacman -Ql <package> [...]

Display information of packages by querying package files: ::

    $ pacman -Qip <pkgfile>  [...]


List all files owned by packages by querying package files: ::

    $ pacman -Qlp <pkgfile> [...]

F
-

Query the files database. This operation allows you to look for packages owning
certain files or display files owned by certain packages. **Only** packages
that are part of your sync databases are searched.

**Note**: The difference between *F* and *Q* options is that the former querys
from files database which cantains both installed and uninstalled packages, but
the later only querys installed pacakges.

F examples
""""""""""

Download fresh package databases from the server, which should always be run
at first: ::

    $ pacman -Fy

Display owners of files (path): ::

    $ pacman -Fo <file> [...]

Display owners of matching strings: ::

    $ pacman -Fs <string> [...]

Display all files owned by packages: ::

    $ pacman -Fl <package> [...]
    
U
-

Upgrade or add package(s) to the system and install the required dependencies
from sync repositories. Either a URL or file path can be specified. This is a
"remove-then-add" process.

U examples
""""""""""

Install from local package file: ::

    # pacman -U <pkg.tar.xz>


Custom local repository
-----------------------

Append a section for the local repository to */etc/pacman.conf*: ::

    # vim /etc/pacman.conf
        [<custom>]
        SigLevel = Optional TrustAll
        Server = file:///home/an9wer/<custompkgs>

Create the repository root and databases: ::

    $ install -d /home/an9wer/<customkgs>
    $ repo-add /home/an9wer/<custompkgs>/custom.db.tar.gz

Add a new package to the database: ::

    $ mv </path/to/pkg.tar.xz> /home/an9wer/<custompkgs>
    $ repo-add /home/an9wer/<custompkgs>/custom.db.tar.gz </path/to/package.tar.xz>

Then install from custom repostiory: ::

    # pacman -Sy <package>

Remove pacakge from database: ::

    $ repo-remove /home/an9wer/<custompkgs>/custom.db.tar.gz <package name>
    $ rm /home/an9wer/<custompkgs>/<pkg.tar.xz>

AUR
---

If you already have a package, initialize it as a Git repository if it is not
one, and add an AUR remote: ::

    $ git init
    $ git remote add origin ssh://aur@aur.archlinux.org/<package>.git
    $ git commit -m "comment"
    $ git branch --set-upstream-to=origin/master
    $ git push origin master

If you are creating a new package from scratch, just clone an unexisted
repository from aur: ::

    $ git clone ssh://aur@aur.archlinux.org/<package>.git


References
""""""""""

``man aur``

`Arch wiki: Custom local repository
<https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks#Custom_local_repository>`_

