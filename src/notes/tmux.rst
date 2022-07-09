Tmux
====

Session
-------

List sessions: ::

    $ tmux ls

Attach a specified session: ::

    $ tmux attach -t <session number>

Close a specified session: ::

    $ tmux kill-session -t <session number>

Close all sessions but a specified session: ::

    $ tmux kill-session -a -t <session number>

Window
------

List windows in a specified session: ::

    $ tmux lsc -t <session number>

Close a specified window: ::

    $ tmux kill-window -t <window number>

Close all windows but a specified window: ::

    $ tmux kill-window -a -t <window number>
