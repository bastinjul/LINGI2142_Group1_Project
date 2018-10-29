#!/bin/bash 

ip link set dev Mi0-eth0 up
ip link add link Mi0-eth0 name Mi0-eth0.140 type vlan id 0x140
ip link set dev Mi0-eth0.140 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Mi0.pid -S Mi0-eth0.140