#!/bin/bash

ROOT='/home/vagrant/LINGI2142_Group1_Project'
sudo mkdir -p $ROOT/dns/zones

for i in 1 2
do
 sudo mkdir -p $ROOT/ucl_minimal_cfg/NS$i/bind/
 sudo mkdir -p $ROOT/ucl_minimal_cfg/NS$i/bind/zones
 sudo mkdir -p /var/log/bind/bind/dns$i.log
 sudo cp $ROOT/dns/zones/* $ROOT/ucl_minimal_cfg/NS$i/bind/zones
 sudo cp $ROOT/dns/named$i.conf* $ROOT/ucl_minimal_cfg/NS$i/bind/
done

for i in 1 2
do
 sudo mv $ROOT/ucl_minimal_cfg/NS$i/bind/named$i.conf $ROOT/ucl_minimal_cfg/NS$i/bind/named.conf
 sudo mv $ROOT/ucl_minimal_cfg/NS$i/bind/named$i.conf.local $ROOT/ucl_minimal_cfg/NS$i/bind/named.conf.local
 sudo mv $ROOT/ucl_minimal_cfg/NS$i/bind/named$i.conf.options $ROOT/ucl_minimal_cfg/NS$i/bind/named.conf.options
done
