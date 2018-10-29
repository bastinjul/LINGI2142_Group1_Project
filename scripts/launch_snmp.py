#!/usr/bin/env python3
import json
import shutil
import os

from constants import PREFIXES, SCRIPTS_PATH, MAIN_PATH, SNMP_FILE_PATH

with open(SCRIPTS_PATH+'configuration_router.json') as data_file:
    data = json.load(data_file)

with open(SCRIPTS_PATH+'configuration_service.json') as data_file:
    data_service = json.load(data_file)


for r in data_service:
	data[r] = data_service[r]

for r in data:
	print("INFO\tStarting SNMP for {} node".format(r))
	os.system('sudo ./snmpd_start.sh ../ucl_minimal_cfg/ {}'.format(r))
