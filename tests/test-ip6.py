#!/usr/bin/env python3
import os, subprocess, re, json

with open('ip-addr.json','a+') as data_file:
    data = json.load(data_file)

os.chdir('../')

print(os.getcwd())

for router in data:
    print(router, data[router])
    for link in router:
        print(link,router[link])
        for prefix in link:
            print(prefix,link[prefix])
            p = subprocess.Popen('ping6 -c 1 -w 100 {}'.format(link[prefix]), stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)

            print(p.communicate())

            print(p.returncode)
