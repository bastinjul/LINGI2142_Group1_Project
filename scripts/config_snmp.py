#!/usr/bin/env python3
import json
import shutil

from constants import PREFIXES, SCRIPTS_PATH, MAIN_PATH, SNMP_DIR_PATH

with open(SCRIPTS_PATH+'configuration_router.json') as data_file:
    data = json.load(data_file)

for r in data:
    shutil.copytree(SNMP_DIR_PATH, MAIN_PATH + 'ucl_minimal_config/'+r)
