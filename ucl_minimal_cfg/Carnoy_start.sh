#!/bin/bash 


ip link set dev Carnoy-eth2 up 
ip address add dev Carnoy-eth2 fd00:200:1:fe42::1/64 
ip address add dev Carnoy-eth2 fd00:300:1:fe42::1/64 
ip link set dev Carnoy-eth0 up 
ip address add dev Carnoy-eth0 fd00:200:1:fe40::1/64 
ip address add dev Carnoy-eth0 fd00:300:1:fe40::1/64 
ip link set dev Carnoy-eth1 up 
ip address add dev Carnoy-eth1 fd00:200:1:fe41::1/64 
ip address add dev Carnoy-eth1 fd00:300:1:fe41::1/64 



/home/vagrant/LINGI2142_Group1_Project/firewall/internal_router.sh

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 


