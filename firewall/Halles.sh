#!/bin/bash

############################
# Settings of the firewall #
############################
# prefix = fd00:200:1 or fd00:300:1
# NS1 address:			prefix:f600::1
# NS2 address:			prefix:f740::1
# Server1 address:		prefix:f600::2
# Server2 address:		prefix:f740::2
# admin addresses: 		prefix:f000::/55
# student addresses:		prefix:f200::/55
# staff addresses:		prefix:f400::/55
# service addresses:		prefix:f600::/55
# guests addresses:		prefix:f800::/55
# others addresses:		prefix:fa00::/55

# reset ip6tables configuration
ip6tables -F

ip6tables -t INPUT -F
ip6tables -t OUTPUT -F
ip6tables -t FORWARD -F

# default policy
# if no rule before matched the packet we drop it
ip6tables -P INPUT DROP
ip6tables -P OUTPUT DROP
ip6tables -P FORWARD DROP

# authorize all the traffic coming from or to an admin user:
for i in 200 300;
do
	ip6tables -A INPUT -s fd00:$i:1:f000::/55 -j ACCEPT
	ip6tables -A OUTPUT -s fd00:$i:1:f000::/55 -j ACCEPT
	ip6tables -A FORWARD -s fd00:$i:1:f000::/55 -j ACCEPT
done
	
# authorize the traffic of an already open connection (ESTABLISHED)
ip6tables -A INPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT
ip6tables -A OUTPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT
ip6tables -A FORWARD -m conntrack --ctstate ESTABLISHED -j ACCEPT

# allow the local traffic (so on the loopback interface) (can't use -i with output)
ip6tables -A INPUT -i lo -j ACCEPT
ip6tables -A FORWARD -i lo -j ACCEPT

# Drop INVALID packets
ip6tables -A INPUT -m state --state INVALID -j DROP 
ip6tables -A OUTPUT -m state --state INVALID -j DROP
ip6tables -A FORWARD -m state --state INVALID -j DROP

# Echo Request (limitation to avoid flooding) type=128/code=0
ip6tables -A INPUT -i belnetb -p icmpv6 --icmpv6-type 128/0 -j ACCEPT --match limit --limit 10/second
ip6tables -A INPUT -i belnetb -p icmpv6 --icmpv6-type 128/0 -j DROP

# ICMPv6 traffic
ip6tables -A INPUT -p icmpv6 -j ACCEPT
ip6tables -A OUTPUT -p icmpv6 -j ACCEPT
ip6tables -A FORWARD -p icmpv6 -j ACCEPT

# allow ospf protocol (but not going/from outside)
# uniquely for border router
#ip6tables -A INPUT -i belnetb -p 89 -j DROP
#ip6tables -A FORWARD -i belnetb -p 89 -j DROP
#ip6tables -A OUTPUT -o belnetb -p 89 -j DROP
#ip6tables -A FORWARD -o belnetb -p 89 -j DROP
# for all routers
ip6tables -A INPUT -p 89 -j ACCEPT
ip6tables -A OUTPUT -p 89 -j ACCEPT
ip6tables -A FORWARD -p 89 -j ACCEPT

# uniquely for border router:
# allow bgp protocol port 179 through tcp but uniquely through the outside interface
ip6tables -A INPUT -i belnetb -p tcp --dport 179 -j ACCEPT
ip6tables -A INPUT -i belnetb -p tcp --sport 179 -j ACCEPT
ip6tables -A OUTPUT -o belnetb -p tcp --dport 179 -j ACCEPT

# uniquely for border router:
# drop packet with our addresses but coming from outside
for i in 200 300;
do
	ip6tables -A INPUT -i belnetb -s fd00:$i:1::/48 -j DROP
	ip6tables -A FORWARD -i belnetb -s fd00:$i:1::/48 -j DROP
done

# DHCP  UDP port number 67 is the destination port of a server, 
# and UDP port number 68 is used by the client. 
for i in 67 68;
do
	ip6tables -A INPUT -p udp --dport $i -j ACCEPT
	ip6tables -A OUTPUT -p udp --dport $i -j ACCEPT
	ip6tables -A FORWARD -p udp --dport $i -j ACCEPT
done

for i in 200 300;
do
	for j in "f600" "f740";
	do
		address=fd00:$i:1:$j::1
		# Allowing Traffic DNS to the two dataserver
		ip6tables -A INPUT -s $address -p udp --dport 53 -j ACCEPT
		ip6tables -A OUTPUT -d $address -p udp --dport 53 -j ACCEPT
		ip6tables -A FORWARD -d $address -p udp --dport 53 -j ACCEPT
	done
done
# We drop the DNS traffic to another address in the network
ip6tables -A INPUT -p udp --dport 53 -j DROP
ip6tables -A INPUT -p tcp --dport 53 -j DROP
# But the DNS traffic for outside of the network is accepted
ip6tables -A OUTPUT -p udp --dport 53 -j ACCEPT
ip6tables -A OUTPUT -p tcp --dport 53 -j ACCEPT
ip6tables -A FORWARD -p udp --dport 53 -j ACCEPT
ip6tables -A FORWARD -p tcp --dport 53 -j ACCEPT

for i in 200 300;
do
	# guest+others+student+staff:
	# HTTP+HTTPS+SMTP+IMAP+POP
	for j in "f200" "f400" "f800" "fa00";
	do
		address=fd00:$i:1:$j::/55
		# http (port 80) and https (port 443)
		for k in 80 443;
		do
			ip6tables -A FORWARD -s $address -p tcp --dport $k -j ACCEPT
		done
	
		# smtp (port 25)
		ip6tables -A FORWARD -s $address -p tcp --dport 25 -j ACCEPT
		
		# pop (port 110 or 995 (with ssl))
		for k in 110 995;
		do
			ip6tables -A FORWARD -s $address -p tcp --dport $k -j ACCEPT
		done
		
		# imap (port 143 or 993 (for imaps but discouraged by RFC 2595))
		for k in 143 993;
		do
			ip6tables -A FORWARD -s $address -p tcp --dport $k -j ACCEPT
		done
	done
	
	# student + staff
	# ssh = tcp through port 22
	for j in "f200" "f400";
	do 
		address=fd00:$i:1:$j::/55
		ip6tables -A FORWARD -s $address -p tcp --dport 22 -j ACCEPT
	done
done

# snmp 
for i in 161 162;
do
	ip6tables -A INPUT -p udp --dport $i -j ACCEPT
	ip6tables -A OUTPUT -p udp --dport $i -j ACCEPT
	ip6tables -A FORWARD -p udp --dport $i -j ACCEPT
	ip6tables -A INPUT -p udp --sport $i -j ACCEPT
	ip6tables -A OUTPUT -p udp --sport $i -j ACCEPT
	ip6tables -A FORWARD -p udp --sport $i -j ACCEPT
done

# uniquely for border router
# block DHCP going/from outside of the network
for i in 546 547;
do
	ip6tables -A INPUT -p udp -i belnetb --dport $i -j DROP
	ip6tables -A FORWARD -p udp -i belnetb --dport $i -j DROP
	ip6tables -A OUTPUT -p udp -o belnetb --dport $i -j DROP
	ip6tables -A FORWARD -p udp -o belnetb --dport $i -j DROP
done

# dhcpv6 port 546 from client and 547 from server the client initialise the connection
ip6tables -A INPUT -p udp --sport 546 --dport 547 -j ACCEPT
ip6tables -A OUTPUT -p udp --sport 546 --dport 547 -j ACCEPT 
ip6tables -A FORWARD -p udp --sport 546 --dport 547 -j ACCEPT
