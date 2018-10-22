#!/usr/bin/env python3
import os, subprocess, re

os.chdir('../')

print(os.getcwd())

p = subprocess.Popen('ping6 -c 1 -w 100 fd00:300::b', stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)

print(p.communicate())

print(p.returncode)








