.. meta::
    :robots: noindex

Docker
======

::

    # docker port <container>
    
::

    # docker inspect <container>


::

    # docker network ls

::

    # docker network inspect <network>

Build
-----

Build from <path>/Dockerfile: ::

    # docker build --tag <image> <path>


Run
---

Run with arguments: ::

    # docker run <image> <arg>...

Run interactively with shell, if no ENTRYPINT set in Dockerfile: ::

    # docker run -it --name <container> <image> /bin/bash

Run interactively with shell, but ENTRYPINT set in Dockerfile: ::

    # docker run -it --name <container> --entrypoint /bin/bash <image>

    or

    # docker run -it --name <container> --entrypoint "" <image> /bin/bash

Remove container after it exits: ::

    # docker run -rm <image>


Volume
------

::

    # docker volume ls

::

    # docker volume inspect <volume>

::

    # docker volume rm <volume>

compose
-------


Installation
""""""""""""

Usage
"""""

::

    # docker-compose up

::

    # docker-compose start <service>

::

    # docker-compose stop <service>

::

    # docker-compose rm <service>

::

    # docker-compose run <service> [<command> ...]

Stop all:

::

    # docker-compose stop

remove all:

::

    # docker-compose rm 

Stop and remove container: ::

    # docker-compose down

Stop and remove container, volumes: ::

    # docker-compose down --volume


Dockerfile
----------

ENTRYPOINT
""""""""""

Exec form: ::

    ENTRYPOINT ["executable", "param1", "param2"]

Shell form: ::

    ENTRYPOINT command param1 param2

An ENTRYPOINT allows you to configure a container that will run as an
executable.

Command line arguments to ``docker run <image>`` will be appended after all
elements in an exec form ENTRYPOINT, and will override all elements specified
using CMD. i.e., ``docker run <image> -d`` will pass the -d argument to the
entry point. 

You can override the ENTRYPOINT instruction using the ``docker run
--entrypoint`` flag.

CMD
"""

As default parameters to ENTRYPOINT: ::

    CMD ["param1","param2"]

Exec form: ::

    CMD ["executable","param1","param2"]

Shell form: ::

    CMD command param1 param2

The main purpose of a CMD is to provide defaults for an executing container.
These defaults can include an executable, or they can omit the executable, in
which case you must specify an ENTRYPOINT instruction as well.

If you list more than one CMD then only the last CMD will take effect.
