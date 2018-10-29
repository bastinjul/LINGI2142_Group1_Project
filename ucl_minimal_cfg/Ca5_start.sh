#!/bin/bash 

ip link set dev Ca5-eth0 up
ip link add link Ca5-eth0 name Ca5-eth0.a45 type vlan id 0xa45
ip link set dev Ca5-eth0.a45 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Ca5.pid -S Ca5-eth0.a45