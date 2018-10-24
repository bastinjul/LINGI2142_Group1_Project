#!/bin/bash 

ip link set dev belnetb up 
ip address add dev belnetb fd00:200::1/48 

ip link set dev Halles-eth1 up 
ip address add dev Halles-eth1 fd00:200:1:ff02::2/64 
ip address add dev Halles-eth1 fd00:300:1:ff02::2/64 
ip link set dev Halles-eth0 up 
ip address add dev Halles-eth0 fd00:200:1:ff00::2/64 
ip address add dev Halles-eth0 fd00:300:1:ff00::2/64 


ip -6 rule add from fd00:300:1::/48 to fd00:200:3::/48 pref 1000 table main 
ip -6 rule add from fd00:300:1::/48 to fd00:300:3::/48 pref 1000 table main 
ip -6 route add ::/0 via fd00:300:1:ff02::4 dev Halles-eth1 metric 1 table 10 
ip -6 rule add from fd00:300:1::/48 pref 2000 table 10 

/home/vagrant/LINGI2142_Group1_Project/firewall/border_router.sh

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 


