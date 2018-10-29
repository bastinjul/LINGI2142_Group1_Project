#!/bin/bash 

ip link set dev Py0-eth0 up
ip link add link Py0-eth0 name Py0-eth0.000 type vlan id 0x000
ip link set dev Py0-eth0.000 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Py0.pid -S Py0-eth0.000