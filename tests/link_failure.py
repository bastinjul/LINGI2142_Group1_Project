#!/usr/bin/env python3
import os, time, json
from print_res import check

print("!!!!! LINK FAILURE TEST BETWEEN SH1C AND HALLES !!!!!")

os.system('sudo ip netns exec SH1C sudo ip link set SH1C-eth1 down')

time.sleep(30)

os.system('./test_all.py')

os.system('sudo ip netns exec SH1C sudo ip link set SH1C-eth1 up')
os.system('sudo ip netns exec SH1C sudo ip address add dev SH1C-eth1 fd00:200:1:ff00::5/64')
os.system('sudo ip netns exec SH1C sudo ip address add dev SH1C-eth1 fd00:300:1:ff00::5/64')

with open('ping_res.json') as ping_file:
        ping_data = json.load(ping_file)

check(ping_data,'PING')

with open('dig_res.json') as dig_file:
        dig_data = json.load(dig_file)

check(dig_data,'DIG')
