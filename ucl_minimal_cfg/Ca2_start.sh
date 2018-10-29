#!/bin/bash 

ip link set dev Ca2-eth0 up
ip link add link Ca2-eth0 name Ca2-eth0.442 type vlan id 0x442
ip link set dev Ca2-eth0.442 up 
