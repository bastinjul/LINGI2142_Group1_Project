#!/usr/bin/env python3
import os, subprocess, re, json, sys, time

def send_trap(data):
    for r in data:
        for add in data[r]:
            if data[r][add] != 0:
                os.system('snmptrap -v2c -c public udp6:[fd00:200:1:f61f::100]:162 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s {}'.format('{} ping failed {}'.format(r,add)))
                os.system('snmptrap -v2c -c public udp6:[fd00:300:1:f61f::100]:162 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s {}'.format('{} ping failed {}'.format(r,add)))
                os.system('snmptrap -v2c -c public udp6:[fd00:200:1:f75f::100]:162 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s {}'.format('{} ping failed {}'.format(r,add)))
                os.system('snmptrap -v2c -c public udp6:[fd00:300:1:f75f::100]:162 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s {}'.format('{} ping failed {}'.format(r,add)))

os.chdir('../tests/')

while True:
    os.system('./test_all')

    with open('ping_res.json') as ping_file:
        ping_data = json.load(ping_file)
    with open('dig_res.json') as dig_file:
        dig_data = json.load(dig_file)

    send_trap(ping_data)
    send_trap(dig_data)

    time.sleep(10)