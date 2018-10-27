#!/bin/bash 

ip link set dev SH2-eth0 up
ip link add link SH2-eth0 name SH2-eth0.582 type vlan id 0x582
ip link set dev SH2-eth0.582 up 
