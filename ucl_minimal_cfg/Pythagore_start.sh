#!/bin/bash 

/home/vagrant/LINGI2142_Group1_Project/firewall/Pythagore.sh

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 

ip link set dev belneta up 
ip address add dev belneta fd00:300::1/48 

ip link set dev Pythagore-eth2 up 
ip address add dev Pythagore-eth2 fd00:200:1:fe00::4/64 
ip address add dev Pythagore-eth2 fd00:300:1:fe00::4/64 
ip link set dev Pythagore-eth1 up 
ip address add dev Pythagore-eth1 fd00:200:1:fe41::4/64 
ip address add dev Pythagore-eth1 fd00:300:1:fe41::4/64 
ip link set dev Pythagore-eth0 up 
ip address add dev Pythagore-eth0 fd00:200:1:ff02::4/64 
ip address add dev Pythagore-eth0 fd00:300:1:ff02::4/64 

ip link set dev Pythagore-lan1 up 
ip address add dev Pythagore-lan1 fd00:200:1:f61f::4/64 
ip address add dev Pythagore-lan1 fd00:300:1:f61f::4/64 
ip link set dev Pythagore-lan0 up 
ip address add dev Pythagore-lan0 fd00:200:1:f600::4/64 
ip address add dev Pythagore-lan0 fd00:300:1:f600::4/64 

ip link set dev Pythagore-lan2 up
ip link add link Pythagore-lan2 name Pyth-lan2.000 type vlan id 0x000
ip link set dev Pyth-lan2.000 up
ip address add dev Pyth-lan2.000 fd00:200:1:f000::/64 
ip address add dev Pyth-lan2.000 fd00:300:1:f000::/64 
ip link add link Pythagore-lan2 name Pyth-lan2.201 type vlan id 0x201
ip link set dev Pyth-lan2.201 up
ip address add dev Pyth-lan2.201 fd00:200:1:f201::/64 
ip address add dev Pyth-lan2.201 fd00:300:1:f201::/64 
ip link add link Pythagore-lan2 name Pyth-lan2.402 type vlan id 0x402
ip link set dev Pyth-lan2.402 up
ip address add dev Pyth-lan2.402 fd00:200:1:f402::/64 
ip address add dev Pyth-lan2.402 fd00:300:1:f402::/64 
ip link add link Pythagore-lan2 name Pyth-lan2.a05 type vlan id 0xa05
ip link set dev Pyth-lan2.a05 up
ip address add dev Pyth-lan2.a05 fd00:200:1:fa05::/64 
ip address add dev Pyth-lan2.a05 fd00:300:1:fa05::/64 

ip -6 rule add from fd00:200:1::/48 to fd00:200:3::/48 pref 1000 table main 
ip -6 rule add from fd00:200:1::/48 to fd00:300:3::/48 pref 1000 table main 
ip -6 route add ::/0 via fd00:200:1:ff02::2 dev Pythagore-eth0 metric 1 table 10 
ip -6 rule add from fd00:200:1::/48 pref 2000 table 10 

