#!/usr/bin/env python3
import os, subprocess, re, json, sys
from test_all import WORKING_NODE

def dig_all_servers(data):
    os.chdir('../')
    res = {}
    com = {}
    for server in data: # routers in the json
        for prefix in data[server]: # address for both as
            address = data[server][prefix]
            p = subprocess.Popen('dig @{} google.com AAAA'.format(address), stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)

            com[address] = p.communicate()

            res[address] = p.returncode
    return res

def write_res(filename,res,node):
    with open(filename,'r') as res1_file:
        res_data = json.load(res1_file)
    res_data[node] = res
    with open(filename,'w') as res2_file:
        res2_file.write(json.dumps(res_data))

node = WORKING_NODE

with open('ns-addr.json','r') as data_file:
    data = json.load(data_file)

res = dig_all_servers(data)
write_res('tests/dig_res.json',res,node)