#!/bin/bash 

ip link set dev NS1-eth0 up 
ip address add dev NS1-eth0 fd00:200:1:f600::1/64 
ip address add dev NS1-eth0 fd00:300:1:f600::1/64 

ip -6 route add ::/0 via fd00:300:1:f600::

named -6 -c /etc/bind/named1.conf
