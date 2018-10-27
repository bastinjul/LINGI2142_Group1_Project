#!/bin/bash 

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 


ip link set dev SH1C-eth0 up 
ip address add dev SH1C-eth0 fd00:200:1:ff41::5/64 
ip address add dev SH1C-eth0 fd00:300:1:ff41::5/64 
ip link set dev SH1C-eth1 up 
ip address add dev SH1C-eth1 fd00:200:1:ff00::5/64 
ip address add dev SH1C-eth1 fd00:300:1:ff00::5/64 


ip link set dev SH1C-lan0 up
ip link add link SH1C-lan0 name SH1C-lan0.180 type vlan id 0x180
ip link set dev SH1C-lan0.180 up
ip address add dev SH1C-lan0.180 fd00:200:1:f180::/64 
ip address add dev SH1C-lan0.180 fd00:300:1:f180::/64 
ip link add link SH1C-lan0 name SH1C-lan0.381 type vlan id 0x381
ip link set dev SH1C-lan0.381 up
ip address add dev SH1C-lan0.381 fd00:200:1:f381::/64 
ip address add dev SH1C-lan0.381 fd00:300:1:f381::/64 
ip link add link SH1C-lan0 name SH1C-lan0.582 type vlan id 0x582
ip link set dev SH1C-lan0.582 up
ip address add dev SH1C-lan0.582 fd00:200:1:f582::/64 
ip address add dev SH1C-lan0.582 fd00:300:1:f582::/64 
ip link add link SH1C-lan0 name SH1C-lan0.b85 type vlan id 0xb85
ip link set dev SH1C-lan0.b85 up
ip address add dev SH1C-lan0.b85 fd00:200:1:fb85::/64 
ip address add dev SH1C-lan0.b85 fd00:300:1:fb85::/64 


