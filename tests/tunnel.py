#!/usr/bin/env python3
import os, time, json
from print_res import check

os.chdir('../')

print("!!!!! LINK FAILURE TEST BETWEEN HALLES AND PYTHAGORE (TO TEST THE TUNNEL) !!!!!")

os.system('sudo ip netns exec Halles sudo ip link set Halles-eth1 down')

time.sleep(30)

os.system('./tests/test_all.py')

os.chdir('ucl_minimal_cfg/')

os.system('sudo ip netns exec Halles sudo ip link set Halles-eth1 up')
os.system('sudo ip netns exec Halles sudo ip address add dev Halles-eth1 fd00:200:1:ff02::2/64')
os.system('sudo ip netns exec Halles sudo ip address add dev Halles-eth1 fd00:300:1:ff02::2/64')

os.chdir('../')

with open('tests/ping_res.json') as ping_file:
        ping_data = json.load(ping_file)

check(ping_data,'PING','')

with open('/tests/dig_res.json') as dig_file:
        dig_data = json.load(dig_file)

check(dig_data,'DIG')
