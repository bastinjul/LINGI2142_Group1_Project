#!/usr/bin/env python3
import json
import os
import stat

from constants import PREFIXES, SCRIPTS_PATH, MAIN_PATH

with open(SCRIPTS_PATH+'configuration_host.json') as data_file:
    data = json.load(data_file)

for host, configs in data.items():

    host_config = open(MAIN_PATH + "ucl_minimal_cfg/" + host + "_start.sh", "w")
    host_config.write("#!/bin/bash \n\n")

    host_eth = host + "-eth0"
    host_config.write("ip link set dev " + host_eth + " up\n")

    host_id_bin = configs["user_bits"] + configs["location_bits"] + "00" + configs["user_bits"]
    host_id = '%03x' % int(host_id_bin, 2)
    host_config.write("ip link add link " + host_eth + " name " + host_eth + "." + host_id + " type vlan id 0x" + host_id + "\n")
    host_config.write("ip link set dev " + host_eth + "." + host_id + " up \n")

    host_config.write("sleep 20; dhclient -6 -pf /var/run/dhclient_" + host + ".pid -S " + host_eth + "." + host_id)

    host_config.close()

    host_boot = open(MAIN_PATH + "ucl_minimal_cfg/" + host + "_boot.sh", "w")
    host_boot.write("#!/bin/bash \n\n")
    host_boot.write("sysctl -p")
    host_boot.close()

    if not os.path.exists(MAIN_PATH + "ucl_minimal_cfg/" + host):
        os.makedirs(MAIN_PATH + "ucl_minimal_cfg/" + host)

    host_sysctl = open(MAIN_PATH + "ucl_minimal_cfg/" + host + "/sysctl.conf", "w")
    host_sysctl.write("net.ipv6.conf.all.disable_ipv6=0\n" + "net.ipv6.conf.all.forwarding=1\n" + "net.ipv6.conf.default.disable_ipv6=0\n" + "net.ipv6.conf.default.forwarding=1")
    host_sysctl.close()

    # Add execution right to _start.sh file
    file_stat = os.stat(MAIN_PATH + "ucl_minimal_cfg/" + host + "_start.sh")
    os.chmod(MAIN_PATH+ "ucl_minimal_cfg/" + host + "_start.sh", file_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    # Add execution right to _boot.sh file
    file_stat = os.stat(MAIN_PATH + "ucl_minimal_cfg/" + host + "_boot.sh")
    os.chmod(MAIN_PATH+ "ucl_minimal_cfg/" + host + "_boot.sh", file_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

