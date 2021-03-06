#!/bin/bash 

/home/vagrant/LINGI2142_Group1_Project/firewall/Halles.sh

puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules 

ip link set dev belnetb up 
ip address add dev belnetb fd00:200::1/48 

ip address add fd00:200:1:ff0f::2 dev lo

ip link set dev Halles-eth0 up 
ip address add dev Halles-eth0 fd00:200:1:ff00::2/64 
ip address add dev Halles-eth0 fd00:300:1:ff00::2/64 
ip link set dev Halles-eth1 up 
ip address add dev Halles-eth1 fd00:200:1:ff02::2/64 
ip address add dev Halles-eth1 fd00:300:1:ff02::2/64 


ip link set dev Halles-lan0 up
ip link add link Halles-lan0 name Halles-lan0.100 type vlan id 0x100
ip link set dev Halles-lan0.100 up
ip address add dev Halles-lan0.100 fd00:200:1:f100::/64 
ip address add dev Halles-lan0.100 fd00:300:1:f100::/64 
ip link add link Halles-lan0 name Halles-lan0.301 type vlan id 0x301
ip link set dev Halles-lan0.301 up
ip address add dev Halles-lan0.301 fd00:200:1:f301::/64 
ip address add dev Halles-lan0.301 fd00:300:1:f301::/64 
ip link add link Halles-lan0 name Halles-lan0.502 type vlan id 0x502
ip link set dev Halles-lan0.502 up
ip address add dev Halles-lan0.502 fd00:200:1:f502::/64 
ip address add dev Halles-lan0.502 fd00:300:1:f502::/64 
ip link add link Halles-lan0 name Halles-lan0.b05 type vlan id 0xb05
ip link set dev Halles-lan0.b05 up
ip address add dev Halles-lan0.b05 fd00:200:1:fb05::/64 
ip address add dev Halles-lan0.b05 fd00:300:1:fb05::/64 

ip -6 rule add from fd00:300:1::/48 to fd00:200:1::/48 pref 1000 table main 
ip -6 rule add from fd00:300:1::/48 to fd00:300:1::/48 pref 1000 table main 
ip -6 route add ::/0 via fd00:300:1:ff02::4 dev Halles-eth1 metric 1 table 10 
ip -6 rule add from fd00:300:1::/48 pref 2000 table 10 
ip -6 tunnel add tun mode ip6ip6 local fd00:200:1:ff0f::2 remote fd00:200:1:fe0f::4 dev lo 
ip link set dev tun up 
ip address add dev tun fd00:200:1:ffff::2/64 
ip -6 route add ::/0 via fd00:200:1:ffff::4 dev tun pref 50 table 10 

