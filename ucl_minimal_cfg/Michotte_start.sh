#!/bin/bash 

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 


ip link set dev Michotte-eth0 up 
ip address add dev Michotte-eth0 fd00:200:1:ff41::3/64 
ip address add dev Michotte-eth0 fd00:300:1:ff41::3/64 
ip link set dev Michotte-eth1 up 
ip address add dev Michotte-eth1 fd00:200:1:fe40::3/64 
ip address add dev Michotte-eth1 fd00:300:1:fe40::3/64 

ip link set dev Michotte-lan0 up 
ip address add dev Michotte-lan0 fd00:200:1:f740::/64 
ip address add dev Michotte-lan0 fd00:300:1:f740::/64 


