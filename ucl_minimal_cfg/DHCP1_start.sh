#!/bin/bash 

ip link set dev DHCP1-eth0 up 
ip address add dev DHCP1-eth0 fd00:200:1:f600::2/64 
ip address add dev DHCP1-eth0 fd00:300:1:f600::2/64 

ip -6 route add ::/0 via fd00:300:1:f600::4

dhcpd -q -6 -f -cf /etc/dhcp/dhcpd6.conf 
