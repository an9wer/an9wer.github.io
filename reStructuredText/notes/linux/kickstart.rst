Kickstart
=========

In CentOS 7, plug in a usb, when load into boot menu page, type TAB key, append
following contents to kernel line:

::

    inst.ks=http://<ip1>:<port>/<ks.cfg> ip=<ip2>::<gateway>:<netmask>:<hostname>:<interface>:none



References
----------

`CentOS docs: kickstart2 <https://docs.centos.org/en-US/centos/install-guide/Kickstart2/>`_

`Wikipedia: PXE <https://en.wikipedia.org/wiki/Preboot_Execution_Environment>`_
