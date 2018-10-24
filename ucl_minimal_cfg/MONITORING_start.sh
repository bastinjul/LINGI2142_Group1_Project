#!/bin/bash 

ip link set dev MONITORING-eth0 up 
ip address add dev MONITORING-eth0 fd00:200:1:f61f::100/64 
ip address add dev MONITORING-eth0 fd00:300:1:f61f::100/64 

ip -6 route add ::/0 via fd00:300:1:f61f::4

