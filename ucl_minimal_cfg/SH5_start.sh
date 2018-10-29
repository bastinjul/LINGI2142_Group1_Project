#!/bin/bash 

ip link set dev SH5-eth0 up
ip link add link SH5-eth0 name SH5-eth0.b85 type vlan id 0xb85
ip link set dev SH5-eth0.b85 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_SH5.pid -S SH5-eth0.b85