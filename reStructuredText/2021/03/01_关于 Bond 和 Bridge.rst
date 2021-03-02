关于 Boud 和 Bridge
===================

遇到这样一种网络情况：一个 AP，一台交换机，一个软路由，想让 AP 和交换机都连接到
软路由上，且在同一个网段，该如何配置呢？

只有一些思路，需要动手在 Gentoo 上做下验证，既然难得不怕麻烦折腾网络，当然需要
记录下。

Static IP
---------

将软路由的 enp1s0 和 enp2s0 分别配置成同一网段的不同 IP： ::

    # vim /etc/conf/net
        config_enp1s0="172.24.0.1/24"
        config_enp2s0="172.24.0.2/24"
    # ln -s /etc/init.d/net.lo /etc/init.d/net.enp1s0
    # ln -s /etc/init.d/net.lo /etc/init.d/net.enp2s0
    # rc-service enp1s0 start
    # rc-service enp2s0 start
        
同时，配置 ``172.24.0.0/24`` 网段的 DHCP Server，分别用两台电脑连接到软路由的
enp1s0 和 enp2s0。

连接到 enp1s0 的电脑 A 和软路由之间可以互相 ping 通，但是连接到 enp2s0 的电脑 B
无法 ping 通软路由。

究其原因是软路由里面有两个关于 ``172.24.0.0/24`` 网段的规则： ::

    172.24.0.0/24 dev enp1s0 proto kernel scope link src 172.24.0.1
    172.24.0.0/24 dev enp2s0 proto kernel scope link src 172.24.0.2

由于第一条关于 ``172.24.0.0/24`` 网段的路由的优先级更高，所以 ping 包在回程的时
候走了第一条路由规则，无法到达电脑 B。


Bond
----

将软路由的 enp1s0 和 enp2s0 配置成 bond： ::

    # vim /etc/conf/net
        config_enp1s0="null"
        config_enp2s0="null"
        slaves_bond0="enp1s0 enp2s0"
        config_bond0="172.24.0.1/24"
    # ln -s /etc/init.d/net.lo /etc/init.d/net.bond0
    # rc-service net.bond0 start

同时，配置 ``172.24.0.0/24`` 网段的 DHCP server，分别用两台电脑连接到软路由的
enp1s0 和 enp2s0。

结果两台电脑和软路由之间可以 ping 通，但是两台电脑之间却不能，即使开启
``net.ipv4.ip_forward`` 还是 unreachable 。

Bridge
------

将软路由的 enp1s0 和 enp2s0 配置成 bridge： ::

    # vim /etc/conf/net
        config_enp1s0="null"
        config_enp2s0="null"
        bridge_br0="enp1s0 enp2s0"
        config_br0="172.24.0.1/24"

同时，配置 ``172.24.0.0/24`` 网段的 DHCP server，分别用两台电脑连接到软路由的
enp1s0 和 enp2s0。

结果两台电脑和软路由之间可以 ping 通，但是两台电脑之间也能 ping 通。

又测试了另外一种 bridge 的方案，即不给 bridge 配置 IP： ::

    # vim /etc/conf/net
        config_enp1s0="null"
        config_enp2s0="null"
        bridge_br0="enp1s0 enp2s0"
        config_br0="null"

此时因为 bridge 没有配置 IP，即没有所属的网段，所以无法配置 DHCP server，只能手
动给两台电脑分配 IP。

结果两台电脑之间可以 ping 通。

Conclusion
----------

忽地理解了 bond 是用来聚合的，bridge 是用来串通的。

所以此场景下还是得用 bridge。

Thanks for reading :)
