#!/usr/bin/env python3
import os, subprocess, re, json, sys
from test_all import WORKING_NODE

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

def write_res(filename,res,node):
    """
        Read the res json and write the result
    """
    with open(filename,'r') as res1_file:
        res_data = json.load(res1_file)
    res_data[node] = res
    with open(filename,'w') as res2_file:
        res2_file.write(json.dumps(res_data))

node = WORKING_NODE

with open('ip-addr.json','r') as data_file:
    data = json.load(data_file)

res = ping_all_routers(data)
print_ping_result(res)
write_res('tests/ping_res.json',res,node)
