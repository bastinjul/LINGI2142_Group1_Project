#!/bin/bash 

ip link set dev Ca1-eth0 up
ip link add link Ca1-eth0 name Ca1-eth0.241 type vlan id 0x241
ip link set dev Ca1-eth0.241 up 
sleep 20; dhclient -6 -pf /var/run/dhclient_Ca1.pid -S Ca1-eth0.241