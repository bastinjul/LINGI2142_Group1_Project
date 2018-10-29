#!/bin/bash 

ip link set dev Ha2-eth0 up
ip link add link Ha2-eth0 name Ha2-eth0.502 type vlan id 0x502
ip link set dev Ha2-eth0.502 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Ha2.pid -S Ha2-eth0.502