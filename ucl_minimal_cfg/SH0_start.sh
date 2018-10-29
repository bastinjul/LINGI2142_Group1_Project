#!/bin/bash 

ip link set dev SH0-eth0 up
ip link add link SH0-eth0 name SH0-eth0.180 type vlan id 0x180
ip link set dev SH0-eth0.180 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_SH0.pid -S SH0-eth0.180