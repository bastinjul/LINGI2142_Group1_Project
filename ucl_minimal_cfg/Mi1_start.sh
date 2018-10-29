#!/bin/bash 

ip link set dev Mi1-eth0 up
ip link add link Mi1-eth0 name Mi1-eth0.341 type vlan id 0x341
ip link set dev Mi1-eth0.341 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Mi1.pid -S Mi1-eth0.341