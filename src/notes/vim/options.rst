.. meta::
    :robots: noindex

Vim Options
===========

paste
    Put vim in paste mode. This will avoid unexpected effects when pasting text
    in insert mode.

cryptmethod cm
    Method used for encryption when the buffer is written to a file.

    -   zip: PkZip compatible method. A weak kind of encryption.

    -   blowfish: Blowfish method. Medium strong encryption but it has an
        implementation flaw.

    -   blowfish2: Blowfish method. Medium strong encryption. This adds a
        "seed" to the file, every time you write the file the encrypted bytes
        will be different.

lhsearch

shortmess

regexpengine

modeline
    If starting editing a new file, and the 'modeline' option is on, a number
    of lines at the beginning and end of the file are checked for modelines.

magic
