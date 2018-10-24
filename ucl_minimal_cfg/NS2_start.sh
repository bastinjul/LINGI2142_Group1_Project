#!/bin/bash 

ip link set dev NS2-eth0 up 
ip address add dev NS2-eth0 fd00:200:1:f740::1/64 
ip address add dev NS2-eth0 fd00:300:1:f740::1/64 

ip -6 route add ::/0 via fd00:200:1:f740::3

named -6 -c /etc/bind/named2.conf 
