; BIND reverse data file for empty rfc1918 zone
;
; DO NOT EDIT THIS FILE - it is used for multiple zones.
; Instead, copy it, edit named.conf, and use that copy.
;
$TTL	86400
@	IN	SOA	group1.ingi. group1.ingi. (
			      1		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			  86400 )	; Negative Cache TTL
;
@	IN	NS	ns1.group1.ingi.
@	IN	NS	ns2.group1.ingi.
ns1	IN	AAAA	fd00:200:1:f600::1
ns1	IN	AAAA	fd00:300:1:f600::1
ns2	IN	AAAA	fd00:200:1:F740::1
ns2	IN	AAAA	fd00:300:1:f740::1