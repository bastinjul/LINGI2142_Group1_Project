#!/bin/bash 

ip link set dev Ha2-eth0 up
ip link add link Ha2-eth0 name Ha2-eth0.502 type vlan id 0x502
ip link set dev Ha2-eth0.502 up 
