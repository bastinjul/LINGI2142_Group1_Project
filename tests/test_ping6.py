#!/usr/bin/env python3
import os, subprocess, re, json, sys
from test_all import WORKING_NODE as node

def ping_all_routers(data):
    os.chdir('../')
    res = {}
    com = {}
    for router in data: # routers in the json
        for link in data[router]: # all link connected to the router
            for prefix in data[router][link]: # address for both as
                address = data[router][link][prefix]
                p = subprocess.Popen('ping6 -c 1 -w 100 {}'.format(address), stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
                
                com[address] = p.communicate()

                res[address] = p.returncode
    return res

def print_ping_result(res):
    for add in res:
        if res[add] == 0:
            print("Ping to the address {} from the {} node:\t\tSUCCESS".format(add,node))
        else:
            print("Ping to the address {} from the {} node:\t\tFAILED".format(add,node))

def write_res(filename,res):
    with open(filename) as data_file:
        res_data = json.load(data_file)
    
    res_data[node] = res

    with open(filename,'w') as data_file:
        data_file.write(res_data)

with open('ip-addr.json') as data_file:
    data = json.load(data_file)

res = ping_all_routers
print_ping_result(res)
write_res('ping_res.js',res)
