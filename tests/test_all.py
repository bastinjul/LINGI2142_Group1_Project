#!/usr/bin/env python3
import os, subprocess, re, json, sys, time

DIG = 'test_dig.py'
PING = 'test_ping6.py'
BGP = 'test_bgp.py'
WORKING_NODE = 'Nope'
RUN = './run_test.sh'
CONFIG = '../ucl_minimal_cfg/'

with open('ip-addr.json') as data_file:
    data = json.load(data_file)

def test_proto(data,proto):
    global WORKING_NODE
    for r in data:
        WORKING_NODE = r
        p = subprocess.Popen('sudo {} {} {} {}'.format(RUN, CONFIG, r, proto), stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
        print(p.communicate)
        time.sleep(0.5) # in order to leave time for the test to complete

test_proto(data,PING)
test_proto(data,DIG)
test_proto(data,BGP)
