#!/bin/bash 

ip link set dev St2-eth0 up
ip link add link St2-eth0 name St2-eth0.482 type vlan id 0x482
ip link set dev St2-eth0.482 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_St2.pid -S St2-eth0.482