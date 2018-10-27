#!/bin/bash

cd
sudo /etc/init.d/bind9 stop
sudo cp bind9.service /etc/systemd/system/bind9.service
sudo systemctl reenable bind9
sudo mkdir -p /var/bind9/chroot/{etc,dev,var/cache/bind,var/run/named}
sudo mknod /var/bind9/chroot/dev/null c 1 3
sudo mknod /var/bind9/chroot/dev/random c 1 8
sudo mknod /var/bind9/chroot/dev/urandom c 1 9
sudo chmod 660 /var/bind9/chroot/dev/{null,random,urandom}
sudo mv /etc/bind /var/bind9/chroot/etc
sudo ln -s /var/bind9/chroot/etc/bind /etc/bind
sudo cp /etc/localtime /var/bind9/chroot/etc/
sudo chown bind:bind /var/bind9/chroot/etc/bind/rndc.key
sudo chmod 775 /var/bind9/chroot/var/{cache/bind,run/named}
sudo chgrp bind /var/bind9/chroot/var/{cache/bind,run/named}

sudo echo "\$AddUnixListenSocket /var/bind9/chroot/dev/log" > /etc/rsyslog.d/bind-chroot.conf
sudo /etc/init.d/rsyslog restart
sudo /etc/init.d/bind9 start
