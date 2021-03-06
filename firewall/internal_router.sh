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
# student addresses:	prefix:f200::/55
# staff addresses:		prefix:f400::/55
# service addresses:	prefix:f600::/55
# guests addresses:		prefix:f800::/55
# others addresses:		prefix:fa00::/55

# reset ip6tables configuration
ip6tables -F

ip6tables -t INPUT -F
ip6tables -t OUTPUT -F
ip6tables -t FORWARD -F

# Any router as for now

# default policy
# if no rule before matched the packet we drop it
ip6tables -P INPUT DROP
ip6tables -P OUTPUT DROP
ip6tables -P FORWARD DROP

# authorize the traffic of an already open connection (ESTABLISHED)
ip6tables -A INPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT
ip6tables -A OUTPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT
ip6tables -A FORWARD -m conntrack --ctstate ESTABLISHED -j ACCEPT

# allow the local traffic (so on the loopback interface) (can't use -i with OUTPUT)
ip6tables -A INPUT -i lo -j ACCEPT
ip6tables -A OUTPUT -o lo -j ACCEPT

# Drop INVALID packets
ip6tables -A INPUT -m state --state INVALID -j DROP
ip6tables -A OUTPUT -m state --state INVALID -j DROP
ip6tables -A FORWARD -m state --state INVALID -j DROP

# authorize all the traffic coming from or to an admin user:
for i in 200 300;
do
	ip6tables -A INPUT -s fd00:$i:1:f000::/55 -j ACCEPT
	ip6tables -A OUTPUT -d fd00:$i:1:f000::/55 -j ACCEPT
	ip6tables -A FORWARD -s fd00:$i:1:f000::/55 -j ACCEPT
	ip6tables -A FORWARD -d fd00:$i:1:f000::/55 -j ACCEPT
done

# Allow tunneling
ip6tables -A INPUT  -p 41 -j ACCEPT
ip6tables -A OUTPUT  -p 41 -j ACCEPT
ip6tables -A FORWARD  -p 41 -j ACCEPT

# ICMPv6 traffic (no limitation for inside traffic)
ip6tables -A INPUT -p icmpv6 -j ACCEPT
ip6tables -A OUTPUT -p icmpv6 -j ACCEPT
ip6tables -A FORWARD -p icmpv6 -j ACCEPT

# allow ospf protocol
ip6tables -A INPUT -p 89 -j ACCEPT
ip6tables -A OUTPUT -p 89 -j ACCEPT
ip6tables -A FORWARD -p 89 -j ACCEPT

for i in 200 300;
do
	for j in "udp" "tcp";
	do
		# Allowing Traffic DNS to the two dataserver
		ip6tables -A FORWARD -d fd00:$i:1:f600::1 -p $j --dport 53 -j ACCEPT
		ip6tables -A FORWARD -d fd00:$i:1:f740::1 -p $j --dport 53 -j ACCEPT
		
		# Allowing Router to make DNS requests for the tests
		ip6tables -A OUTPUT -d fd00:$i:1:f600::1 -p $j --dport 53 -j ACCEPT
		ip6tables -A OUTPUT -d fd00:$i:1:f740::1 -p $j --dport 53 -j ACCEPT
		
		# We drop the DNS traffic in destination to another address in the network
		ip6tables -A FORWARD -d fd00:$i:1::/64 -p $j --dport 53 -j DROP
		# But the DNS traffic for outside of the network is accepted
		ip6tables -A FORWARD -p $j --dport 53 -j ACCEPT
	done
done

for i in 200 300;
do
	# guest+others+student+staff:
	# HTTP+HTTPS+SMTP+IMAP+POP
	for j in "f200" "f400" "f800" "fa00";
	do
		address=fd00:$i:1:$j::/55
		# http (port 80) and https (port 443)
		ip6tables -A FORWARD -s $address -p tcp -m multiport --dports 80,443 -j ACCEPT

		# smtp (port 25)
		ip6tables -A FORWARD -s $address -p tcp --dport 25 -j ACCEPT

		# pop (port 110 or 995 (with ssl))
		ip6tables -A FORWARD -s $address -p tcp -m multiport --dports 110,995 -j ACCEPT

		# imap (port 143 or 993 (for imaps but discouraged by RFC 2595))
		ip6tables -A FORWARD -s $address -p tcp -m multiport --dports 143,993 -j ACCEPT
	done

	# student + staff
	# ssh = tcp through port 22
	for j in "f200" "f400";
	do
		address=fd00:$i:1:$j::/55
		ip6tables -A FORWARD -s $address -p tcp --dport 22 -j ACCEPT
	done
	
	# Allowing Traffic DHCPv6 to the two DHCPservers
	ip6tables -A FORWARD -d fd00:$i:1:f600::2 -p udp --sport 546 --dport 547 -j ACCEPT
	ip6tables -A FORWARD -d fd00:$i:1:f740::2 -p udp --sport 546 --dport 547 -j ACCEPT
done

# snmp
ip6tables -A INPUT -p udp -m multiport --dports 161,162 -j ACCEPT
ip6tables -A OUTPUT -p udp -m multiport --dports 161,162 -j ACCEPT
ip6tables -A FORWARD -p udp -m multiport --dports 161,162 -j ACCEPT
ip6tables -A INPUT -p udp -m multiport --sports 161,162 -j ACCEPT
ip6tables -A OUTPUT -p udp -m multiport --sports 161,162 -j ACCEPT
ip6tables -A FORWARD -p udp -m multiport --sports 161,162 -j ACCEPT

