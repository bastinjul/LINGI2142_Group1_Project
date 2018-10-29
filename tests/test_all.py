#!/usr/bin/env python3
import os, subprocess, re, json, sys, time

PING = 'test_ping6.py'
WORKING_NODE = 'Nope'
RUN = './run_test.sh'
CONFIG = '../ucl_minimal_cfg/'

with open('ip-addr.json') as data_file:
    data = json.load(data_file)

def test_ping(data):
    global WORKING_NODE
    for r in data:
        WORKING_NODE = r
        p = subprocess.Popen('sudo {} {} {} {}'.format(RUN, CONFIG, r, PING), stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
        print(p.communicate)
        time.sleep(0.5)

test_ping(data)

