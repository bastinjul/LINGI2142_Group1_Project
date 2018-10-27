#!/bin/bash 

ip link set dev Py1-eth0 up
ip link add link Py1-eth0 name Py1-eth0.201 type vlan id 0x201
ip link set dev Py1-eth0.201 up 
