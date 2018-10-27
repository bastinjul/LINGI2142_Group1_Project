#!/bin/bash 

ip link set dev Ca5-eth0 up
ip link add link Ca5-eth0 name Ca5-eth0.a45 type vlan id 0xa45
ip link set dev Ca5-eth0.a45 up 
