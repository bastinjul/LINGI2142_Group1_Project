#!/bin/bash 

ip link set dev Mi5-eth0 up
ip link add link Mi5-eth0 name Mi5-eth0.b45 type vlan id 0xb45
ip link set dev Mi5-eth0.b45 up 
