#!/usr/bin/env python3
import os
from print_res import check

print("!!!!! STANDARD TEST FOR PING AND DIG !!!!!")

os.system('./test_all')

with open('ping_res.json') as ping_file:
        ping_data = json.load(ping_file)

check(ping_data,'PING')

with open('dig_res.json') as dig_file:
        dig_data = json.load(dig_file)

check(dig_data,'DIG')
