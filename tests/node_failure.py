#!/usr/bin/env python3
import os, time, json
from print_res import check

print("!!!!! ROUTER FAILURE OF SH1C !!!!!")

os.system('sudo ip netns exec SH1C sudo kill "$(< /tmp/HALL_bird.pid)"')
os.system('sudo ip netns exec SH1C sudo ip link set SH1C-eth0 down')
os.system('sudo ip netns exec SH1C sudo ip link set SH1C-eth1 down')

time.sleep(30)

os.system('./test_all.py')

os.system('sudo ip netns exec SH1C sudo ip link set SH1C-eth1 up')
os.system('sudo ip netns exec SH1C sudo ip address add dev SH1C-eth1 fd00:200:1:ff00::5/64')
os.system('sudo ip netns exec SH1C sudo ip address add dev SH1C-eth1 fd00:300:1:ff00::5/64')

with open('ping_res.json') as ping_file:
        ping_data = json.load(ping_file)

check(ping_data,'PING')

with open('dig_res.json') as dig_file:
        dig_data = json.load(dig_file)

check(dig_data,'DIG')


echo "[TEST] Router failure test"
echo "[INFO] Shut down HALL"
sudo ip netns exec HALL sudo kill "$(< /tmp/HALL_bird.pid)"
sudo ip netns exec HALL sudo ip link set HALL-eth0 down
sudo ip netns exec HALL sudo ip link set HALL-eth1 down
sudo ip netns exec HALL sudo ip link set HALL-eth2 down

echo "[INFO] Waiting for network to stabilize (30 sec)"
sleep 30

echo "[INFO] Launching host connectivity test"
echo "[INFO] These addresses should be unreachable : fd00:X00:3:1::1 fd00:X00:3:2::1 fd00:X00:3:7::1 fd00:200:3:100::53 fd00:200:3:100::80"
echo "[INFO] Routers can not reach fd00:300::b because they still use the 300 prefix by default."
echo "[INFO] Host HA1 can not reach the rest of the network because it is on the VLAN of HALL."
sudo /home/vagrant/lingi2142/routing_test/host_connectivity.sh

echo ""
echo "[INFO] Turn BIRD daemon on HALL back on"
sudo ip netns exec HALL sudo bird6 -s /tmp/HALL.ctl -P /tmp/HALL_bird.pid &
sudo ip netns exec HALL sudo ip link set HALL-eth0 up
sudo ip netns exec HALL sudo ip address add fd00:200:3:7::1/64 dev HALL-eth0
sudo ip netns exec HALL sudo ip address add fd00:300:3:7::1/64 dev HALL-eth0
sudo ip netns exec HALL sudo ip link set HALL-eth1 up
sudo ip netns exec HALL sudo ip address add fd00:200:3:1::1/64 dev HALL-eth1
sudo ip netns exec HALL sudo ip address add fd00:300:3:1::1/64 dev HALL-eth1
sudo ip netns exec HALL sudo ip link set HALL-eth2 up
sudo ip netns exec HALL sudo ip address add fd00:200:3:2::1/64 dev HALL-eth2
sudo ip netns exec HALL sudo ip address add fd00:300:3:2::1/64 dev HALL-eth2