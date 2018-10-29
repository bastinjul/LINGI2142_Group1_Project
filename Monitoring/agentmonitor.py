import os
import time
# PySNMP High Level API. Commands: bulkCmd, getCmd, nextCmd and setCmd
from pysnmp.hlapi import *
from pysnmp.smi.view import MibViewController
# Data types used by PySNMP
from pyasn1.type.univ import * 
# Multithreading
import threading
# SNMP getter functions
from snmpfun import *

# author: Maxime Mawait, inspired from https://makina-corpus.com/blog/metier/2016/initiation-a-snmp-avec-python-pysnmp-partie2

"""AGENT MONITOR"""
class Agent_monitor(threading.Thread):
    def __init__(self, stop_event, agent, ip, db_directory, snmpv3_user, data_collect_funs):
        threading.Thread.__init__(self)
        self.agent = agent
        self.stop_event = stop_event
        self.ip = ip
        self.db_directory = db_directory
        self.snmpv3_user = snmpv3_user
        self.data_collect_funs = data_collect_funs

    def run(self):
        # Instantiate SNMP engine
        snmp_engine = SnmpEngine()

        # Specify which MIB to use
        mib_view_controller = snmp_engine.getUserContext('mibViewController')
        if not mib_view_controller:
            mib_view_controller = MibViewController(snmp_engine.getMibBuilder())

        # Instantiate user - SNMPv3
        user = UsmUserData(**self.snmpv3_user)

        # Instantiate transport protocol (UDP over IPv6)
        upd_target = Udp6TransportTarget((self.ip, SNMP_PORT)) 

        while not self.stop_event.is_set():
            for data_collect_fun in self.data_collect_funs:
                data_collect_fun(snmp_engine, user, upd_target, self.db_directory)
            # Wait before getting next data
            stop_event.wait(TIME_INTERVAL)


"""MONITORING INITIALIZATION"""
# Infos
threads = []
stop_event = threading.Event()
snmpv3_user = {   
                'userName': 'gr1', 
                'authProtocol': usmHMACSHAAuthProtocol, # SHA (128bit)
                'authKey': 'password',
                'privKey': 'secret_key',
                'privProtocol': usmAesCfb128Protocol # AES (128bit)
            }

# Open conf file and initiate threads
with open('agent_list.conf', 'r') as f:
    for line in f:
        agent_name, agent_ip = line.split()
        print(agent_name,agent_ip)
        db_directory = os.path.join('monitoring', agent_name)
        if not os.path.exists(db_directory):
            os.makedirs(db_directory)
        initialize_ip_info_db(db_directory)
        threads.append(Agent_monitor(stop_event, agent_name, agent_ip, db_directory, snmpv3_user, [ip_info]))

# Start monitoring each agent
for th in threads:
    th.start()

# Stop monitoring
if input('Type "stop" to terminate all threads\n') == 'stop':
    print('Terminating all threads...')
    stop_event.set()
    for th in threads:
        th.join()


