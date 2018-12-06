#!/usr/bin/env python3
# author: Maxime Mawait, inspired from http://snmplabs.com/pysnmp/examples/v3arch/asyncore/manager/ntfrcv/snmp-versions.html
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp6
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.proto.api import v2c

# Create SNMP engine with autogenernated engineID and pre-bound
# to socket transport dispatcher
snmpEngine = engine.SnmpEngine()

# Transport setup

# UDP over IPv6, first listening interface/port
config.addTransport(
    snmpEngine,
    udp6.domainName + (1,),
    udp6.Udp6Transport().openServerMode(('::', 162))
)

# UDP over IPv6, second listening interface/port
config.addTransport(
    snmpEngine,
    udp6.domainName + (2,),
    udp6.Udp6Transport().openServerMode(('::', 2162))
)

# SNMPv1/2c setup

# SecurityName <-> CommunityName mapping
config.addV1System(snmpEngine, 'my-area', 'public')

config.addV3User(
    snmpEngine, 'usr-sha-aes128',
    config.usmHMACSHAAuthProtocol, 'authkey1',
    config.usmAesCfb128Protocol, 'privkey1'
)


# Callback function for receiving notifications
# noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
def cbFun(snmpEngine, stateReference, contextEngineId, contextName,
          varBinds, cbCtx):
    print('Notification from ContextEngineId "%s", ContextName "%s"' % (contextEngineId.prettyPrint(),
                                                                        contextName.prettyPrint()))
    with open('trap.log','a') as f:    
        for name, val in varBinds:
                print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                f.write('%s = %s\n' % (name.prettyPrint(), val.prettyPrint()))

# Register SNMP Application at the SNMP engine
ntfrcv.NotificationReceiver(snmpEngine, cbFun)

snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish

# Run I/O dispatcher which would receive queries and send confirmations
try:
    snmpEngine.transportDispatcher.runDispatcher()
except:
    snmpEngine.transportDispatcher.closeDispatcher()
    raise
