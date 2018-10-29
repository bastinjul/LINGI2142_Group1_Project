#!/bin/bash 

ip link set dev Py2-eth0 up
ip link add link Py2-eth0 name Py2-eth0.402 type vlan id 0x402
ip link set dev Py2-eth0.402 up 
