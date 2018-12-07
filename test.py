#!/usr/bin/env python3

import os

os.chdir('tests/')

os.system('./standard.py')
os.system('./link_failure.py')
os.system('./tunnel.py')