#!/bin/bash 

ip link set dev Ha5-eth0 up
ip link add link Ha5-eth0 name Ha5-eth0.b05 type vlan id 0xb05
ip link set dev Ha5-eth0.b05 up 
