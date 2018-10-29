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
                    'DEF:ip_received='+db_location+':received:AVERAGE',
                    'DEF:ip_size='+db_location+':size:AVERAGE',
                    'DEF:ip_delivered='+db_location+':delivered:AVERAGE',
                    'DEF:ip_forwarded='+db_location+':forwarded:AVERAGE',
                    'CDEF:ip_not_delivered=ip_received,ip_delivered,-,ip_forwarded,-',
                    'LINE1:ip_received#00FF00:Total Received',
                    'LINE1:ip_size#00FF00:Input size of data in Bytes',
                    'LINE1:ip_delivered#FF0000:Delivered',
                    'LINE1:ip_forwarded#070070:Forwarded',
                    'LINE1:ip_not_delivered#0000FF:Not delivered',
                    )

with open('agent_list.conf', 'r') as f:
    for line in f:
        agent_name, agent_ip = line.split()
        db_directory = os.path.join('monitoring', agent_name)
        if not os.path.exists(db_directory):
            os.makedirs(db_directory)
        graph_ip_info(db_directory)