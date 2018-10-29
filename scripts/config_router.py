#!/usr/bin/env python3
import json

from constants import PREFIXES, SCRIPTS_PATH, MAIN_PATH

with open(SCRIPTS_PATH+'configuration_router.json') as data_file:
    data = json.load(data_file)

for router, configs in data.items():

    start_config = open(MAIN_PATH + "ucl_minimal_cfg/" + router + "_start.sh", "w")
    start_config.write("#!/bin/bash \n\n")
        # for bgp

    if router == "Pythagore":
        start_config.write(MAIN_PATH + "firewall/Pythagore.sh\n\n")
    elif router == "Halles":
        start_config.write(MAIN_PATH + "firewall/Halles.sh\n\n")
    else:
        start_config.write(MAIN_PATH + "firewall/internal_router.sh\n\n")
    start_config.write("puppet apply --verbose --parser future --hiera_config=/etc/puppet/hiera.yaml /etc/puppet/site.pp --modulepath=/puppetmodules \n\n")



    for isp, isp_conf in configs["isp"].items():
        start_config.write("ip link set dev " + isp + " up \n")
        start_config.write("ip address add dev " + isp + " " + isp_conf["self_address"] + " \n")

    start_config.write("\n")

    # for links between routers

    for eth, bits in configs["eths"].items():
        start_config.write("ip link set dev " + router + "-" + eth + " up \n")
        for prefix in PREFIXES:
            prefix_end_bits = "1111111" + configs["location_bits"] + bits
            neighbor = configs["neighbor"]
            neighbor_eth = neighbor[eth]
            neighbor_params = neighbor_eth.split("-")
            neighbor_configs = data[neighbor_params[0]]
            neighbor_id = neighbor_configs["router_id"]
            if(configs["router_id"] > neighbor_id):
                neighbor_eth_configs = neighbor_configs["eths"]
                prefix_end_bits = "1111111" + neighbor_configs["location_bits"] + neighbor_eth_configs[neighbor_params[1]]

            prefix_end = '%04x' % int(prefix_end_bits, 2)
            start_config.write("ip address add dev " + router + "-" + eth + " " + prefix + prefix_end + "::" + configs["router_id"] + "/64 \n")

    start_config.write("\n")

    #Service configuration

    for lan, end_prefix in configs["lans"].items():
        start_config.write("ip link set dev " + router + "-" + lan + " up \n")
        for prefix in PREFIXES:
            prefix_end_bits = "1111011" + configs["location_bits"] + end_prefix
            prefix_end = '%04x' % int(prefix_end_bits, 2)
            start_config.write("ip address add dev " + router + "-" + lan + " " + prefix + prefix_end + "::" + configs["router_id"] + "/64 \n")

    start_config.write("\n")

    #host configuration

    router_vlan = router + "-" + configs["vlan"]
    router_lan = router + "-" + configs["vlan"]
    if router == "Pythagore":
        router_vlan = "Pyth" + "-" + configs["vlan"]
    if router == "Michotte":
        router_vlan = "Mich" + "-" + configs["vlan"]
    start_config.write("ip link set dev " + router_lan + " up\n")

    users = ["000", "001", "010", "101"]
    for u in users:
        host_id_bin = u + configs["location_bits"] + "00" + u
        host_id = '%03x' % int(host_id_bin, 2)
        start_config.write("ip link add link " + router_lan + " name " + router_vlan + "." + host_id + " type vlan id 0x" + host_id +"\n")
        start_config.write("ip link set dev " + router_vlan + "." + host_id + " up\n")
        for prefix in PREFIXES:
            start_config.write("ip address add dev " + router_vlan + "." + host_id + " " + prefix + "f" + host_id + "::/64 \n")

    start_config.write("\n")

    if "extra_ip_command" in configs:
        for command in configs["extra_ip_command"]:
            start_config.write(command + " \n")

    start_config.write("\n")

    start_config.close()

