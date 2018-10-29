#!/bin/bash 

ip link set dev Py2-eth0 up
ip link add link Py2-eth0 name Py2-eth0.402 type vlan id 0x402
ip link set dev Py2-eth0.402 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Py2.pid -S Py2-eth0.402