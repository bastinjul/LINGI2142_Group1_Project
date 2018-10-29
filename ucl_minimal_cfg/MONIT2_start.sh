#!/bin/bash 

ip link set dev MONIT2-eth0 up 
ip address add dev MONIT2-eth0 fd00:200:1:f75f::100/64 
ip address add dev MONIT2-eth0 fd00:300:1:f75f::100/64 

ip -6 route add ::/0 via fd00:200:1:f75f::3

