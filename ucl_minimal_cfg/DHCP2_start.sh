#!/bin/bash 

ip link set dev DHCP2-eth0 up 
ip address add dev DHCP2-eth0 fd00:200:1:f740::2/64 
ip address add dev DHCP2-eth0 fd00:300:1:f740::2/64 

ip -6 route add ::/0 via fd00:200:1:f740::3

