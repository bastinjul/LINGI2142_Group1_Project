#!/usr/bin/env python3
import os, time, json
from print_res import check

print("!!!!! ROUTER FAILURE OF SH1C !!!!!")

os.system('sudo ip netns exec SH1C sudo kill "$(< /tmp/SH1C_bird.pid)"')
os.system('sudo ip netns exec SH1C sudo ip link set SH1C-eth0 down')
os.system('sudo ip netns exec SH1C sudo ip link set SH1C-eth1 down')

time.sleep(30)

os.system('./test_all.py')

os.chdir('../ucl_minimal_cfg/')

os.system('sudo ip netns exec SH1C sudo bird6 -s /tmp/SH1C.ctl -P /tmp/SH1C_bird.pid &')
os.system('sudo ip netns exec SH1C sudo ip link set SH1C-eth1 up')
os.system('sudo ip netns exec SH1C sudo ip address add dev SH1C-eth1 fd00:200:1:ff00::5/64')
os.system('sudo ip netns exec SH1C sudo ip address add dev SH1C-eth1 fd00:300:1:ff00::5/64')
os.system('sudo ip netns exec SH1C sudo ip link set SH1C-eth0 up')
os.system('sudo ip netns exec SH1C sudo ip address add dev SH1C-eth0 fd00:200:1:ff41::5/64')
os.system('sudo ip netns exec SH1C sudo ip address add dev SH1C-eth0 fd00:300:1:ff41::5/64')

os.chdir('../tests/')

with open('ping_res.json') as ping_file:
        ping_data = json.load(ping_file)

check(ping_data,'PING')

with open('dig_res.json') as dig_file:
        dig_data = json.load(dig_file)

check(dig_data,'DIG')

with open('bgp_res.json') as bgp_file:
        bgp_data = json.load(bgp_file)

check(bgp_data,'BGP')
