Linux process
=============

Zombie process
--------------

https://en.wikipedia.org/wiki/Zombie_process
     a zombie process or defunct process is a process that has completed
     execution (via the exit system call) but still has an entry in the process
     table.

     How to generate a zombie process?

     Run *supervisord* in non-daemon mode, type Ctrl-Z to put it in backgroud,
     kill some subprocess managed by *supervisord*, and run `ps` command to
     check the state of that subprocess which should be *defunct*.


Orphan process
--------------

https://en.wikipedia.org/wiki/Orphan_process
    In a Unix-like operating system any orphaned process will be immediately
    adopted by the special init system process: the kernel sets the parent to
    init. This operation is called re-parenting and occurs automatically.

    How to generate a orphan process?

    Run *supervisord* in daemon mode, kill *supervisord* process only, and run
    `ps` comand to check PPID of subprocess managed by *supervisord* which
    should be 1.

    It is sometimes desirable to intentionally orphan a process, usually to
    allow a long-running job to complete without further user attention, or to
    start an indefinitely running service or agent; such processes (without an
    associated session) are known as daemons, particularly if they are
    indefinitely running.


Whan happened of child process when parent process is dead?
    The child process will become orphan process.

    https://unix.stackexchange.com/questions/158727/is-there-any-unix-variant-on-which-a-child-process-dies-with-its-parent

