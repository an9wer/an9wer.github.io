Vim Pattern
===========

See *:h pattern.txt*

g*
    Search forward for the word nearest to the cursor, like "*", but don't put
    "\<" and "\>" around the word.

g#
    Search backword for the word nearst to the cursor, like "#", but don't put
    "\<" and "\>" around the word.


A pattern contains one or more branches (multiple branched are seperated by
"\|"). (see *:h /pattern*)

a branch contains one or more contacts (multiple contacts are seperated by
"\&"). (see *:h /branch*)

a contact contains one or more pieces. (see *:h /contact*)

a piece is an atom. (see *:h /piece*)

an atom can be one of a long list of items (use "\(" to group pattern into an
atom). (see *:h /atom*)


To clear last used search pattern:

::

    :set @/= ""
