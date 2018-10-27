#!/bin/bash 

ip link set dev Py5-eth0 up
ip link add link Py5-eth0 name Py5-eth0.a05 type vlan id 0xa05
ip link set dev Py5-eth0.a05 up 
