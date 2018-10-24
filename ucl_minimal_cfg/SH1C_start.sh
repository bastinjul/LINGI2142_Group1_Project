#!/bin/bash 


ip link set dev SH1C-eth0 up 
ip address add dev SH1C-eth0 fd00:200:1:ff41::5/64 
ip address add dev SH1C-eth0 fd00:300:1:ff41::5/64 
ip link set dev SH1C-eth1 up 
ip address add dev SH1C-eth1 fd00:200:1:ff00::5/64 
ip address add dev SH1C-eth1 fd00:300:1:ff00::5/64 



/home/vagrant/LINGI2142_Group1_Project/firewall/internal_router.sh

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 


