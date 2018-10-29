#!/bin/bash 

ip link set dev Ca0-eth0 up
ip link add link Ca0-eth0 name Ca0-eth0.040 type vlan id 0x040
ip link set dev Ca0-eth0.040 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Ca0.pid -S Ca0-eth0.040