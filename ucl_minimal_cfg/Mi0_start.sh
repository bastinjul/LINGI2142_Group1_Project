#!/bin/bash 

ip link set dev Mi0-eth0 up
ip link add link Mi0-eth0 name Mi0-eth0.140 type vlan id 0x140
ip link set dev Mi0-eth0.140 up 
