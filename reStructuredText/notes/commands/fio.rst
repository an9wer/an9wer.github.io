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


References
----------

`Fio official document <https://fio.readthedocs.io/en/latest/fio_doc.html>`_

`Wikipedia: standard deviation <https://en.wikipedia.org/wiki/Standard_deviation>`_
