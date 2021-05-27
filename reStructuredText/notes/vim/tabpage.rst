.. meta::
    :robots: noindex

Vim Tabpage
===========

See ``:h tabpage``

Commands
--------

{count}gt | :{count}tabn[ext]
    Go to tab page {count}. The first tab page has number one.

{count}gT | :{count}tabp[revious]
    Go to the previous tab page.

CTRL-W gf
    Open a new tab page and edit the file name under the cursor.

:[count]tabnew
    Open a new tab page with an empty window.

    ::

        :tabnew	    " opens tabpage after the current one
        :.tabnew    " as above
        :+tabnew    " opens tabpage after the next tab page, note: it is one further than :tabnew
        :-tabnew    " opens tabpage before the current one
        :0tabnew    " opens tabpage before the first one
        :$tabnew    " opens tabpage after the last one

    
:[N]tabm[ove] | :tabm[ove] [N]
    Move the current tab page to after tab page N.

    ::

		:.tabmove	" do nothing
		:-tabmove	" move the tab page to the left
		:+tabmove	" move the tab page to the right
		:0tabmove	" move the tab page to the beginning of the tab list
		:tabmove 0	" as above
		:tabmove	" move the tab page to the last
		:$tabmove	" as above
		:tabmove $	" as above
    

Tabline
-------

See ``:h setting-tabline``
