#!/usr/bin/env python3
import os, subprocess, re, json, sys
from test_all import WORKING_NODE
from print_res import write_res

def ping_all_as(data):
    os.chdir('../')
    res = {}
    com = {}
    for as_router in data: # routers in the json
        address = data[as_router]
        p = subprocess.Popen('ping6 -c 1 -w 100 {}'.format(address), stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)

        com[address] = p.communicate()

        res[address] = p.returncode
    return res

node = WORKING_NODE

with open('as-addr.json','r') as data_file:
    data = json.load(data_file)

res = ping_all_as(data)
write_res('tests/bgp_res.json',res,node)
