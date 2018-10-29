#!/usr/bin/env python3
import os, subprocess, re, json, sys

with open('ip-addr.json') as data_file:
    data = json.load(data_file)

os.chdir('../')

def ping_all_routers(data):
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
            print("Ping to the address {} from the {} node:\t\tSUCCESS".format(add,sys.argv[1]))
        else:
            print("Ping to the address {} from the {} node:\t\tFAILED".format(add,sys.argv[1]))