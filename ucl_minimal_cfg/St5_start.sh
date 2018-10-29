#!/bin/bash 

ip link set dev St5-eth0 up
ip link add link St5-eth0 name St5-eth0.a85 type vlan id 0xa85
ip link set dev St5-eth0.a85 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_St5.pid -S St5-eth0.a85