#!/bin/bash 

ip link set dev Ha1-eth0 up
ip link add link Ha1-eth0 name Ha1-eth0.301 type vlan id 0x301
ip link set dev Ha1-eth0.301 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Ha1.pid -S Ha1-eth0.301