NPD
===

Install requirements:

::

    $ python2 -m virtualenv venv
    $ source venv/bin/activate
    $ pip install sqlalchemy
    $ pip install tornado

Dump disk enclosure to json:

::

    $ IFS=. read -ra hostname <<< $HOSTNAME
    $ ls /sys/class/enclosure/* | awk '$1=="SLOT" && $2~/,./ {print $2}' | awk -v HOSTNAME=${hostname[0]} -F, 'BEGIN{printf("[")} {if(NR>1)printf(", "); printf("{\"host\":\"%s\", \"panel\":5, \"row\":%d, \"col\":%d, \"serial\": \"%s\", \"optype\": 1}", HOSTNAME, $1 / 6 + 1, $1 % 6 + 1, $2)} END{printf("]")}' 

Dump json to db:

::

    $ source venv/bin/activate
    $ cd src
    $ python diskdb.py --db ../db/wuxi_disks.db apply_ios_json --source <json file>

Run webserver to check:

::

    $ source venv/bin/activate
    $ cd src
    $ python main.py --db=../db/wuxi_disks.db --port=<port number>
