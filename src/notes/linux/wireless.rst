.. meta::
    :robots: noindex

Linux wireless
==============

Frequency band
--------------

The 802.11 standard provides several distinct radio frequency ranges for use in
Wi-Fi communications: 900 MHz, 2.4 GHz, 3.6 GHz, 4.9 GHz, 5 GHz, 5.9 GHz and 60
GHz bands. Each range is divided into a multitude of channels.

Channel
-------

todo


Transmission power
------------------

The high TX power will extend the range for slower TX rates only, as faster
rates are transmitted at a lower TX power, which is normal for ALL APs and
devices. 

Signal level
------------

+-----------------+-----------+------------------------------------------------+
| Signal Strength | TL;DR     |                                                |
+=================+===========+================================================+
| -30 dBm         | Amazing   | Max achievable signal strength. The client can |
|                 |           | only be a few feet from the AP to achieve this.|
|                 |           | Not typical or desirable in the real world.    |
+-----------------+-----------+------------------------------------------------+
| -67 dBm         | Very Good | Minimum signal strength for applications that  |
|                 |           | require very reliable, timely packet delivery. |
+-----------------+-----------+------------------------------------------------+
| -70 dBm         | Okay      | Minimum signal strength for reliable packet    |
|                 |           | delivery.                                      |
+-----------------+-----------+------------------------------------------------+
| -80 dBm         | Not Good  | Minimum signal strength for basic connectivity.|
|                 |           | Packet delivery may be unreliable.             |
+-----------------+-----------+------------------------------------------------+
| -90 dBm         | Unusable  | Approaching or drowning in the noise floor. Any|
|                 |           | functionality is highly unlikely.              |
+-----------------+-----------+------------------------------------------------+

wireless_tools
--------------

Get frequency (channel) of connected wireless: ::

    $ iwconfig | grep Frequency

Get TX power of connected wireless: ::

    $ iwconfig | grep Tx-Power

Get speed (bit rate) of connected wireless: ::

    $ iwconfig | grep 'Bit Rate'

Get signal level of connected wireless: ::

    $ iwconfig | grep 'Signal level'

List supported channel of wireless interface: ::

    $ iwlist <dev> channel

iw
--

::

    iw list



References
----------

`Linux kernel wiki: wireless dirvers
<https://wireless.wiki.kernel.org/en/users/drivers>`_

`Arch wiki: wireless network configuration
<https://wiki.archlinux.org/index.php/Wireless_network_configuration>`_

`Archwiki: software access point
<https://wiki.archlinux.org/index.php/software_access_point>`_

`Ubuntu: wifi master mode
<https://help.ubuntu.com/community/WifiDocs/MasterMode>`_

`Wikipedia: Comparison of open-source wireless drivers
<https://en.wikipedia.org/wiki/Comparison_of_open-source_wireless_drivers>`_

`Wikipedia: List of WLAN channels
<https://en.wikipedia.org/wiki/List_of_WLAN_channels>`_

`Frequencies bands, channels and bandwidth
<https://www.electronics-notes.com/articles/connectivity/wifi-ieee-802-11/channels-frequencies-bands-bandwidth.php>`_

https://www.reddit.com/r/linuxquestions/comments/52r2nh/is_is_possible_to_split_a_single_wireless_nic/
