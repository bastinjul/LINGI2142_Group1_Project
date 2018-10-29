#!/usr/bin/env python3
import json
import shutil
import os

from constants import PREFIXES, SCRIPTS_PATH, MAIN_PATH, SNMP_FILE_PATH, USER, SNMP_CONF

with open(SCRIPTS_PATH+'configuration_router.json') as data_file:
    data = json.load(data_file)

with open(SCRIPTS_PATH+'configuration_service.json') as data_file:
    data_service = json.load(data_file)


for r in data_service:
	data[r] = data_service[r]

for r in data:
	print("INFO\tConfiguring SNMP for {} node".format(r))
	if not os.path.exists(MAIN_PATH + 'ucl_minimal_cfg/'+r+'/snmp/'):
		print("INFO\tCreating SNMP Configuration directory")
		os.makedirs(MAIN_PATH + 'ucl_minimal_cfg/'+r+'/snmp/')
	print("INFO\tCopying SNMP Configuration file")
	shutil.copy(SNMP_FILE_PATH,MAIN_PATH + 'ucl_minimal_cfg/'+r+'/snmp/')
	os.system('sudo chown vagrant:vagrant {}ucl_minimal_cfg/{}/{}'.format(MAIN_PATH,r,SNMP_CONF))
