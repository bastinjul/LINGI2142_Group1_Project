#!/bin/bash 

ip link set dev Ca0-eth0 up
ip link add link Ca0-eth0 name Ca0-eth0.040 type vlan id 0x040
ip link set dev Ca0-eth0.040 up 
