#!/bin/bash 

ip link set dev St0-eth0 up
ip link add link St0-eth0 name St0-eth0.080 type vlan id 0x080
ip link set dev St0-eth0.080 up 
