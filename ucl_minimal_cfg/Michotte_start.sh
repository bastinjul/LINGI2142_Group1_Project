#!/bin/bash 

/home/vagrant/LINGI2142_Group1_Project/firewall/internal_router.sh

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 


ip address add fd00:200:1:ff4f::3 dev lo

ip link set dev Michotte-eth1 up 
ip address add dev Michotte-eth1 fd00:200:1:fe40::3/64 
ip address add dev Michotte-eth1 fd00:300:1:fe40::3/64 
ip link set dev Michotte-eth0 up 
ip address add dev Michotte-eth0 fd00:200:1:ff41::3/64 
ip address add dev Michotte-eth0 fd00:300:1:ff41::3/64 

ip link set dev Michotte-lan0 up 
ip address add dev Michotte-lan0 fd00:200:1:f740::3/64 
ip address add dev Michotte-lan0 fd00:300:1:f740::3/64 
ip link set dev Michotte-lan2 up 
ip address add dev Michotte-lan2 fd00:200:1:f75f::3/64 
ip address add dev Michotte-lan2 fd00:300:1:f75f::3/64 

ip link set dev Michotte-lan1 up
ip link add link Michotte-lan1 name Mich-lan1.140 type vlan id 0x140
ip link set dev Mich-lan1.140 up
ip address add dev Mich-lan1.140 fd00:200:1:f140::/64 
ip address add dev Mich-lan1.140 fd00:300:1:f140::/64 
ip link add link Michotte-lan1 name Mich-lan1.341 type vlan id 0x341
ip link set dev Mich-lan1.341 up
ip address add dev Mich-lan1.341 fd00:200:1:f341::/64 
ip address add dev Mich-lan1.341 fd00:300:1:f341::/64 
ip link add link Michotte-lan1 name Mich-lan1.542 type vlan id 0x542
ip link set dev Mich-lan1.542 up
ip address add dev Mich-lan1.542 fd00:200:1:f542::/64 
ip address add dev Mich-lan1.542 fd00:300:1:f542::/64 
ip link add link Michotte-lan1 name Mich-lan1.b45 type vlan id 0xb45
ip link set dev Mich-lan1.b45 up
ip address add dev Mich-lan1.b45 fd00:200:1:fb45::/64 
ip address add dev Mich-lan1.b45 fd00:300:1:fb45::/64 


