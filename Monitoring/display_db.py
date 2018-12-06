import os
import sys
import tempfile
import rrdtool 

GRAPH_START = '-1000'
GRAPH_END = 'now'
                    
def graph_ip_info(db_directory):
    db_location = os.path.join(db_directory, 'ip.rrd')
    img_location = os.path.join(db_directory, 'ip.png')
    rrdtool.graph(  img_location,
                    '--width', '1080',
                    '--height', '300',
                    '--start', GRAPH_START,
                    '--end', GRAPH_END,
                    '--vertical-label', 'datagrams/s',
                    '--title', 'IP',
                    '--lower-limit', '0',
                    'DEF:received='+db_location+':received:AVERAGE',
                    'DEF:hdrerror='+db_location+':hdrerror:AVERAGE',
                    'DEF:addrerror='+db_location+':addrerror:AVERAGE',
                    'DEF:unknownprotos='+db_location+':unknowprotos:AVERAGE',
                    'DEF:forwarded='+db_location+':forwarded:AVERAGE',
                    'DEF:discarded='+db_location+':discarded:AVERAGE',
                    'DEF:delivered='+db_location+':delivered:AVERAGE',
                    'DEF:outrequests='+db_location+':outrequests:AVERAGE',
                    'DEF:outnoroutes='+db_location+':outnoroutes:AVERAGE',
                    'DEF:outdiscards='+db_location+':outdiscards:AVERAGE',
                    'CDEF:errors=hdrerror,addrerror,+,unknownprotos,+,outnoroutes,+',
                    'CDEF:discards=discarded,outdiscards,+',
                    'LINE1:received#00FF00:Total Received',
                    'LINE1:errors#0000FF:Errors',
                    'LINE1:delivered#FF0000:Delivered',
                    'LINE1:forwarded#070070:Forwarded',
                    'LINE1:outrequests#070070:Request for out datagramms',
                    'LINE1:discards#0000FF:Discarded'
                    )

with open('agent_list.conf', 'r') as f:
    for line in f:
        agent_name, agent_ip = line.split()
        db_directory = os.path.join('monitoring', agent_name)
        if not os.path.exists(db_directory):
            os.makedirs(db_directory)
        graph_ip_info(db_directory)
