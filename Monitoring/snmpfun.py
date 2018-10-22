import os
# PySNMP High Level API. Commands: bulkCmd, getCmd, nextCmd and setCmd
from pysnmp.hlapi import *
from pysnmp.smi.view import MibViewController
# Data types used by PySNMP
from pyasn1.type.univ import * 
# Round-Robin Database 
import rrdtool 

"""CONSTANTS"""
TIME_INTERVAL = 10
TIME_WAIT_VALUE = 15
SNMP_PORT = 161 # Default port


"""USEFUL FUNCTIONS"""
def update_rrd(snmp_engine, user, upd_target, data, db_location):
    """Updates the database given as argument with the data received in response to an SNMP GET request"""
    # Get data from agent
    get_data = getCmd(  snmp_engine,
                        user,
                        upd_target,
                        ContextData(),
                        *data)

    errorIndication, errorStatus, errorIndex, varBinds = next(get_data)
    if errorIndication:
        print(errorIndication)
        return 'error'
    elif errorStatus:
        print('%s at %s' % (
                                errorStatus.prettyPrint(), 
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'
                            )
        )
        return 'error'
    else:
        rrd_cmd='N'
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
            rrd_cmd += ':' + val.prettyPrint()
        rrdtool.update(db_location, rrd_cmd)


"""DB INITIALIZATION FUNCTIONS"""
def initialize_ram_info_db(db_directory):
    db_location = os.path.join(db_directory, 'ram_usage.rrd')
    rrdtool.create( db_location, 
                    '--start', 'now', 
                    '--step', str(TIME_INTERVAL), 
                    'DS:used:GAUGE:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:free:GAUGE:'+str(TIME_WAIT_VALUE)+':0:U', 
                    'RRA:AVERAGE:0.5:1:100')

def initialize_cpu_info_db(db_directory):
    db_location = os.path.join(db_directory, 'cpu_usage.rrd')
    rrdtool.create( db_location, 
                    '--start', 'now', 
                    '--step', str(TIME_INTERVAL), 
                    'DS:user:GAUGE:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:system:GAUGE:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:idle:GAUGE:'+str(TIME_WAIT_VALUE)+':0:U', 
                    'DS:nice:GAUGE:'+str(TIME_WAIT_VALUE)+':0:U', 
                    'RRA:AVERAGE:0.5:1:100')

def initialize_ip_info_db(db_directory):
    db_location = os.path.join(db_directory, 'ip.rrd')
    rrdtool.create( db_location, 
                    '--start', 'now', 
                    '--step', str(TIME_INTERVAL), 
                    'DS:received:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:delivered:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:forwarded:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U', 
                    'RRA:AVERAGE:0.5:1:100')

def initialize_udp_info_db(db_directory):
    db_location = os.path.join(db_directory, 'udp.rrd')
    rrdtool.create( db_location, 
                    '--start', 'now', 
                    '--step', str(TIME_INTERVAL), 
                    'DS:delivered:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:sent:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:notdelivered_noport:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U', 
                    'DS:notdelivered_error:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U', 
                    'RRA:AVERAGE:0.5:1:100')

def initialize_tcp_info_db(db_directory):
    db_location = os.path.join(db_directory, 'tcp.rrd')
    rrdtool.create( db_location, 
                    '--start', 'now', 
                    '--step', str(TIME_INTERVAL), 
                    'DS:received_total:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:received_error:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:sent:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U', 
                    'DS:retransmitted:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U', 
                    'RRA:AVERAGE:0.5:1:100')

"""DATA COLLECTION FUNCTIONS"""
def ram_info(snmp_engine, user, upd_target, db_directory):
    """Collects information about the RAM of an agent"""
    db_location = os.path.join(db_directory, 'ram_usage.rrd')
    data = (
        ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'memAvailReal', 0)),
        ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'memTotalFree', 0))
    )
    update_rrd(snmp_engine, user, upd_target, data, db_location)

def cpu_info(snmp_engine, user, upd_target, db_directory):
    """Collects information about the CPU usage of an agent"""
    db_location = os.path.join(db_directory, 'cpu_usage.rrd')
    data = (
        ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'ssCpuRawUser', 0)), # % user CPU time
        ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'ssCpuRawSystem', 0)), # % system CPU time
        ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'ssCpuRawIdle', 0)), # % idle CPU time
        ObjectType(ObjectIdentity('UCD-SNMP-MIB', 'ssCpuRawNice', 0)) # % nice CPU time
    )
    update_rrd(snmp_engine, user, upd_target, data, db_location)

def ip_info(snmp_engine, user, upd_target, db_directory):
    """Collects information about the IP packets going through this agent's interfaces"""
    db_location = os.path.join(db_directory, 'ip.rrd')
    data = (
        ObjectType(ObjectIdentity('IP-MIB', 'ipInReceives', 0)), # Total number of received input datagrams (including those received in error)
        ObjectType(ObjectIdentity('IP-MIB', 'ipInDelivers', 0)), # Total number of input datagrams successfully delivered to IP user protocols
        ObjectType(ObjectIdentity('IP-MIB', 'ipForwDatagrams', 0)) # Number of input datagrams for which this entity was not their final IP destination
    )
    update_rrd(snmp_engine, user, upd_target, data, db_location)

def udp_info(snmp_engine, user, upd_target, db_directory):
    """Collects information about the UDP datagrams going through this agent's interfaces"""
    db_location = os.path.join(db_directory, 'udp.rrd')
    data = (
        ObjectType(ObjectIdentity('UDP-MIB', 'udpInDatagrams', 0)), # Number of UDP datagrams delivered to UDP users
        ObjectType(ObjectIdentity('UDP-MIB', 'udpOutDatagrams', 0)), # Number of UDP datagrams sent
        ObjectType(ObjectIdentity('UDP-MIB', 'udpNoPorts', 0)), # Number of received UDP datagrams that could not be delivered due to having no app at the destination port
        ObjectType(ObjectIdentity('UDP-MIB', 'udpInErrors', 0)) # Number of received UDP datagrams that could not be delivered (for other reasons)
    )
    update_rrd(snmp_engine, user, upd_target, data, db_location)

def tcp_info(snmp_engine, user, upd_target, db_directory):
    """Collects information about the TCP active connections and TCP segments going through this agent's interfaces"""
    db_location = os.path.join(db_directory, 'tcp.rrd')
    data = (
        ObjectType(ObjectIdentity('TCP-MIB', 'tcpInSegs', 0)), # Number of segments received, including those received in error
        ObjectType(ObjectIdentity('TCP-MIB', 'tcpInErrs', 0)), # Number of segments received in error
        ObjectType(ObjectIdentity('TCP-MIB', 'tcpOutSegs', 0)), # Number of segments sent
        ObjectType(ObjectIdentity('TCP-MIB', 'tcpRetransSegs', 0)) # Number of segments retransmitted
    )
    update_rrd(snmp_engine, user, upd_target, data, db_location)


def pkt_info(snmp_engine, user, upd_target, db_directory):
    pass

