#!/bin/bash 

ip link set dev SH1-eth0 up
ip link add link SH1-eth0 name SH1-eth0.381 type vlan id 0x381
ip link set dev SH1-eth0.381 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_SH1.pid -S SH1-eth0.381