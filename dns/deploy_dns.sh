#!/bin/bash

ROOT='/home/vagrant/lingi2142'
sudo mkdir -p $ROOT/dns/zones
#sudo bash $ROOT/dns_config_creation.sh
for i in 1 2
do
 sudo mkdir -p $ROOT/ucl_minimal_cfg/NS$i/bind/
 sudo mkdir -p $ROOT/ucl_minimal_cfg/NS$i/bind/zones
 sudo mkdir -p /var/log/bind/bind/dns$i.log
 sudo cp $ROOT/dns/utils_dns.py $ROOT/ucl_minimal_cfg/NS$i/bind/
 sudo cp $ROOT/dns/zones/* $ROOT/ucl_minimal_cfg/NS$i/bind/zones
 sudo cp $ROOT/dns/named$i.conf* $ROOT/ucl_minimal_cfg/NS$i/bind/
 sudo cp $ROOT/dns/update_dns.py $ROOT/ucl_minimal_cfg/NS$i/bind/
 chmod +x $ROOT/ucl_minimal_cfg/NS$i/bind/update_dns.py 
done
