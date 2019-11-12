lsof
====

Scan directory (not descend the directory tree): ::

    # lsof +d <directory>

Scan directory, follow symbolic links and/or filesystems: ::

    # lsof +d <directory> -x|-x l|-x f

Scan directory tree (include all subdirectories): ::

    # lsof +D <directory>

Scan directory tree, follow symbolic links and/or filesystems: ::

    # lsof +D <directory> -x|-x l|-x f

Show all open socket file: ::

    # lsof -i [46][protocol][@hostname|@hostaddr][:service|:port]

Show open socket file in specified state: ::

    # lsof -i [46][TCP|UDP][@hostname|@hostaddr][:service|:port] -s TCP|UDP:ESTABLISHED|LISTEN
