#!/bin/bash 

ip link set dev Mi2-eth0 up
ip link add link Mi2-eth0 name Mi2-eth0.542 type vlan id 0x542
ip link set dev Mi2-eth0.542 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Mi2.pid -S Mi2-eth0.542