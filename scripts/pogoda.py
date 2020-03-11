import os,sys
from urllib import request, parse
import re
if len(sys.argv) < 2: exit()
d=parse.urlencode({'name':sys.argv[1]}).encode('utf-8')
req = request.Request('http://www.meteo.pl/um/php/gpp/next.php',data=d,method='POST')
r = request.urlopen(req).readlines()
dat = b''
for row in r:
    dat += row
x = re.findall('show_mgram\\(\\d*\\)',dat.decode('iso-8859-2'))
x = x[0].replace('show_mgram(','').replace(')','')
os.system('start "" "http://www.meteo.pl/um/php/meteorogram_id_um.php?ntype=0u&id={}"'.format(x))
