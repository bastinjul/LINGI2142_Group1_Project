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
def initialize_ip_info_db(db_directory):
    db_location = os.path.join(db_directory, 'ip.rrd')
    rrdtool.create( db_location, 
                    '--start', 'now', 
                    '--step', str(TIME_INTERVAL), 
                    'DS:received:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:delivered:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U',
                    'DS:forwarded:COUNTER:'+str(TIME_WAIT_VALUE)+':0:U', 
                    'RRA:AVERAGE:0.5:1:100')

"""DATA COLLECTION FUNCTIONS"""
def ip_info(snmp_engine, user, upd_target, db_directory):
    """Collects information about the IP packets going through this agent's interfaces"""
    db_location = os.path.join(db_directory, 'ip.rrd')
    data = (
        ObjectType(ObjectIdentity('IP-MIB', 'ipInReceives', 0)), # Total number of received input datagrams (including those received in error)
        ObjectType(ObjectIdentity('IP-MIB', 'ipInHdrErrors', 0)), # The number of input IP datagrams discarded due to errors in their IP headers.
        ObjectType(ObjectIdentity('IP-MIB', 'ipInAddrErrors', 0)), # The number of input IP datagrams discarded because the IP address in their IP header's destination field was not a valid address
        ObjectType(ObjectIdentity('IP-MIB', 'ipInUnknownProtos', 0)), # The number of locally-addressed IP datagrams received successfully but discarded because of an unknown or unsupported protocol
        ObjectType(ObjectIdentity('IP-MIB', 'ipInForwDatagrams', 0)), # The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination
        ObjectType(ObjectIdentity('IP-MIB', 'ipInDiscards', 0)), # The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but were discarded
        ObjectType(ObjectIdentity('IP-MIB', 'ipInDelivers', 0)), # The total number of datagrams successfully delivered to IP user-protocols
        ObjectType(ObjectIdentity('IP-MIB', 'ipOutRequests', 0)), # The total number of IP datagrams that local IP user-protocols  supplied to IP in requests for transmission
        ObjectType(ObjectIdentity('IP-MIB', 'ipOutNoRoutes', 0)), # The number of locally generated IP datagrams discarded because no route could be found to transmit them to their destination
        ObjectType(ObjectIdentity('IP-MIB', 'ipOutDiscards', 0)) # The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but were discarded
    )
    update_rrd(snmp_engine, user, upd_target, data, db_location)


def pkt_info(snmp_engine, user, upd_target, db_directory):
    pass

