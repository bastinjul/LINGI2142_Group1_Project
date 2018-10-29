#!/bin/bash 

/home/vagrant/LINGI2142_Group1_Project/firewall/internal_router.sh

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 


ip link set dev Stevin-eth1 up 
ip address add dev Stevin-eth1 fd00:200:1:fe00::6/64 
ip address add dev Stevin-eth1 fd00:300:1:fe00::6/64 
ip link set dev Stevin-eth0 up 
ip address add dev Stevin-eth0 fd00:200:1:fe42::6/64 
ip address add dev Stevin-eth0 fd00:300:1:fe42::6/64 


ip link set dev Stevin-lan0 up
ip link add link Stevin-lan0 name Stevin-lan0.080 type vlan id 0x080
ip link set dev Stevin-lan0.080 up
ip address add dev Stevin-lan0.080 fd00:200:1:f080::/64 
ip address add dev Stevin-lan0.080 fd00:300:1:f080::/64 
ip link add link Stevin-lan0 name Stevin-lan0.281 type vlan id 0x281
ip link set dev Stevin-lan0.281 up
ip address add dev Stevin-lan0.281 fd00:200:1:f281::/64 
ip address add dev Stevin-lan0.281 fd00:300:1:f281::/64 
ip link add link Stevin-lan0 name Stevin-lan0.482 type vlan id 0x482
ip link set dev Stevin-lan0.482 up
ip address add dev Stevin-lan0.482 fd00:200:1:f482::/64 
ip address add dev Stevin-lan0.482 fd00:300:1:f482::/64 
ip link add link Stevin-lan0 name Stevin-lan0.a85 type vlan id 0xa85
ip link set dev Stevin-lan0.a85 up
ip address add dev Stevin-lan0.a85 fd00:200:1:fa85::/64 
ip address add dev Stevin-lan0.a85 fd00:300:1:fa85::/64 


