#!/bin/bash 

ip link set dev Ha5-eth0 up
ip link add link Ha5-eth0 name Ha5-eth0.b05 type vlan id 0xb05
ip link set dev Ha5-eth0.b05 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Ha5.pid -S Ha5-eth0.b05