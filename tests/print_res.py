#!/usr/bin/env python3
import os, json, time

WA = '!'*3
def check(data,pattern,*discard):
    success = True
    for r in data:
        for d in data[r]:
            if r not in discard and d not in discard and data[r][d] != 0:
                success = False
                print('{0} {1} TEST FAILED FOR {2} ROUTER AND {3} ADDRESS {0}'.format(WA,pattern,r,d))
    if success:
        print('===> {} TEST IS A WONDERFUL SUCCESS'.format(pattern))

def write_res(filename,res,node):
    """
        Read the res json and write the result
    """
    with open(filename,'r') as res1_file:
        res_data = json.load(res1_file)
    res_data[node] = res
    with open(filename,'w') as res2_file:
        res2_file.write(json.dumps(res_data))
