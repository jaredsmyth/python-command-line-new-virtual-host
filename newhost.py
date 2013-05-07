# jared smith
# 2013
# jvst, inc

import sys
import os

hostsDir = '/private/etc/hosts'
vhostsDir = '/private/etc/apache2/extra/httpd-vhosts.conf'

startHostString = '\n\n<VirtualHost *:80>\n    DocumentRoot'
endHostString = '\n</VirtualHost>'

# check for name arg and then save
if len(sys.argv)>1:
	with open(hostsDir, 'a') as hosts:
		hosts.write('\n127.0.0.1 '+sys.argv[1])
else:
	print 'you need to name your new host'

# check for dir arg and then save
if len(sys.argv)<3: 
	with open(vhostsDir, 'a') as vhosts:
		vhosts.write(startHostString+' "'+os.getcwd()+'"\n    Servername '+sys.argv[1]+endHostString) 
else:
	with open(vhostsDir, 'a') as vhosts:
		vhosts.write(startHostString+' "'+sys.argv[2]+'"\n    Servername '+sys.argv[1]+endHostString)