#!/bin/bash 

ip link set dev Ha0-eth0 up
ip link add link Ha0-eth0 name Ha0-eth0.100 type vlan id 0x100
ip link set dev Ha0-eth0.100 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Ha0.pid -S Ha0-eth0.100