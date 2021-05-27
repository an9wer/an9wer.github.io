.. meta::
    :robots: noindex

Fio
===

Interpreting the output
-----------------------

slat
    Submission latency (min being the minimum, max being the maximum, avg being
    the average, stdev being the *standard deviation*). This is the time it
    took to submit the I/O. For sync I/O this row is not displayed as the slat
    is really the completion latency (since queue/complete is one operation
    there).

clat
    Completion latency. This denotes the time from submission to completion of
    the I/O pieces. For sync I/O, clat will usually be equal (or very close) to
    0, as the time from submit to complete is basically just CPU time (I/O has
    already been done, see slat explanation).

lat
    Total latency. This denotes the time from when fio created the I/O unit to
    completion of the I/O operation.

Examples
--------

::

    [global]
    ioengine=libaio
    direct=1
    blocksize=1Mi
    iodepth=32                  # aio 每次提交 32 个 blocksize？
    verify=md5
    do_verify=1
    rw=write                    # 顺序写

    [write]
    directory=/mnt/dbtest
    filesize=1Mi:10Mi           # 文件大小 1m - 10m 中随机（最小必须大于 blocksize 的设置）
    nrfiles=1000                # 总共写 1000 个文件
    
::

    [global]
    ioengine=libaio
    direct=1
    blocksize=4Ki
    iodepth=32
    filesize=200Ki:10Mi         # 文件大小随机从 200Ki 到 10Mi
    nrfiles=1000                # 总共 1000 个文件
    directory=/mnt/dbtest

    [write]
    rw=rw                       # 顺序读写
    rwmixread=0                 # 读占比为0%，也即全部顺序写

    [randread]
    rw=randrw                   # 随机读写
    rwmixwrite=0                # 写占比为 0%，也即全部随机读


References
----------

`Fio official document
<https://fio.readthedocs.io/en/latest/fio_doc.html>`_

`Wikipedia: standard deviation
<https://en.wikipedia.org/wiki/Standard_deviation>`_
