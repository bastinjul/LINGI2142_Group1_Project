#!/bin/bash 

/home/vagrant/LINGI2142_Group1_Project/firewall/internal_router.sh

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 


ip address add fd00:200:1:fe4f::1 dev lo

ip link set dev Carnoy-eth2 up 
ip address add dev Carnoy-eth2 fd00:200:1:fe42::1/64 
ip address add dev Carnoy-eth2 fd00:300:1:fe42::1/64 
ip link set dev Carnoy-eth0 up 
ip address add dev Carnoy-eth0 fd00:200:1:fe40::1/64 
ip address add dev Carnoy-eth0 fd00:300:1:fe40::1/64 
ip link set dev Carnoy-eth1 up 
ip address add dev Carnoy-eth1 fd00:200:1:fe41::1/64 
ip address add dev Carnoy-eth1 fd00:300:1:fe41::1/64 


ip link set dev Carnoy-lan0 up
ip link add link Carnoy-lan0 name Carnoy-lan0.040 type vlan id 0x040
ip link set dev Carnoy-lan0.040 up
ip address add dev Carnoy-lan0.040 fd00:200:1:f040::/64 
ip address add dev Carnoy-lan0.040 fd00:300:1:f040::/64 
ip link add link Carnoy-lan0 name Carnoy-lan0.241 type vlan id 0x241
ip link set dev Carnoy-lan0.241 up
ip address add dev Carnoy-lan0.241 fd00:200:1:f241::/64 
ip address add dev Carnoy-lan0.241 fd00:300:1:f241::/64 
ip link add link Carnoy-lan0 name Carnoy-lan0.442 type vlan id 0x442
ip link set dev Carnoy-lan0.442 up
ip address add dev Carnoy-lan0.442 fd00:200:1:f442::/64 
ip address add dev Carnoy-lan0.442 fd00:300:1:f442::/64 
ip link add link Carnoy-lan0 name Carnoy-lan0.a45 type vlan id 0xa45
ip link set dev Carnoy-lan0.a45 up
ip address add dev Carnoy-lan0.a45 fd00:200:1:fa45::/64 
ip address add dev Carnoy-lan0.a45 fd00:300:1:fa45::/64 


