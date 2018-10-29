#!/usr/bin/env python3
import json
import shutil
import os

from constants import PREFIXES, SCRIPTS_PATH, MAIN_PATH, SNMP_FILE_PATH

with open(SCRIPTS_PATH+'configuration_router.json') as data_file:
    data1 = json.load(data_file)

with open(SCRIPTS_PATH+'configuration_service.json') as data_file:
    data2 = json.load(data_file)

print(data1)
print(data2)

for r in data1:
	if not os.path.exists(MAIN_PATH + 'ucl_minimal_cfg/'+r+'/snmp/'):
		os.makedirs(MAIN_PATH + 'ucl_minimal_cfg/'+r+'/snmp/')
	shutil.copy(SNMP_FILE_PATH,MAIN_PATH + 'ucl_minimal_cfg/'+r+'/snmp/')


for r in data2:
	if not os.path.exists(MAIN_PATH + 'ucl_minimal_cfg/'+r+'/snmp/'):
		os.makedirs(MAIN_PATH + 'ucl_minimal_cfg/'+r+'/snmp/')
	shutil.copy(SNMP_FILE_PATH,MAIN_PATH + 'ucl_minimal_cfg/'+r+'/snmp/')
