#!/usr/bin/env python3
import json
import os
import stat

from constants import PREFIXES, SCRIPTS_PATH, MAIN_PATH

with open(SCRIPTS_PATH+'configuration_service.json') as data_file:
    data = json.load(data_file)

for service, configs in data.items():

    service_config = open(MAIN_PATH + "ucl_minimal_cfg/" + service + "_start.sh", "w")
    service_config.write("#!/bin/bash \n\n")

    interface = service + "-eth0"
    service_config.write("ip link set dev " + interface + " up \n")

    for prefix in PREFIXES:
        prefix_end_bits = "1111011" + configs["location_bits"] + configs["sub_network_prefix"]
        prefix_end = '%04x' % int(prefix_end_bits, 2)
        service_config.write("ip address add dev " + interface + " " + prefix + prefix_end + configs["end_address"] + "/64 \n")

    service_config.write("\nip -6 route add ::/0 via " + configs["default_route"] + "\n")

    service_config.close()

    service_boot = open(MAIN_PATH + "ucl_minimal_cfg/" + service + "_boot.sh", "w")
    service_boot.write("#!/bin/bash \n\n")
    service_boot.write("sysctl -p")
    service_boot.close()

    #service_sysctl = open(MAIN_PATH + "ucl_minimal_cfg/" + service + "/sysctl.conf", "w")
    #service_sysctl.write("net.ipv6.conf.all.disable_ipv6=0\n" + "net.ipv6.conf.all.forwarding=1\n" + "net.ipv6.conf.default.disable_ipv6=0\n" + "net.ipv6.conf.default.forwarding=1")
    #service_sysctl.close()

    # Add execution right to _start.sh file
    file_stat = os.stat(MAIN_PATH + "ucl_minimal_cfg/" + service + "_start.sh")
    os.chmod(MAIN_PATH+ "ucl_minimal_cfg/" + service + "_start.sh", file_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    # Add execution right to _boot.sh file
    file_stat = os.stat(MAIN_PATH + "ucl_minimal_cfg/" + service + "_boot.sh")
    os.chmod(MAIN_PATH+ "ucl_minimal_cfg/" + service + "_boot.sh", file_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

