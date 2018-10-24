#!/bin/bash 


ip link set dev Stevin-eth1 up 
ip address add dev Stevin-eth1 fd00:200:1:fe00::6/64 
ip address add dev Stevin-eth1 fd00:300:1:fe00::6/64 
ip link set dev Stevin-eth0 up 
ip address add dev Stevin-eth0 fd00:200:1:fe42::6/64 
ip address add dev Stevin-eth0 fd00:300:1:fe42::6/64 



/home/vagrant/LINGI2142_Group1_Project/firewall/internal_router.sh

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 


