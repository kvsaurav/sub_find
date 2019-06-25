 
#python2

import dnsdumpster
import os

from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI #USING DNSDUMPSTER.COM API
print "ENTER DOMAIN TO BE SEARCHED"
g= raw_input('')
res = DNSDumpsterAPI({'verbose': True}).search(g)

print res.keys() 

for item in res['dns_records']['host']:

	print "*"*80
	print "\n\n"
	print "DOMAIN: ", item['domain'].replace('<br', '')
	print "IP ADRESS: ",item['ip']
	print "PROVIDER :",item['provider']
	print "REVERSE DNS :",item['reverse_dns']