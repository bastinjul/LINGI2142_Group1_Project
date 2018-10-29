#!/bin/bash 

ip link set dev St1-eth0 up
ip link add link St1-eth0 name St1-eth0.281 type vlan id 0x281
ip link set dev St1-eth0.281 up 
