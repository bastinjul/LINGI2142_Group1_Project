#!/bin/bash 

ip link set dev Py5-eth0 up
ip link add link Py5-eth0 name Py5-eth0.a05 type vlan id 0xa05
ip link set dev Py5-eth0.a05 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Py5.pid -S Py5-eth0.a05