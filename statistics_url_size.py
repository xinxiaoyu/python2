#!/usr/bin/env python

import re
import subprocess

f = open(r'/newdisk/root/access_json.log','r')
f1 = open(r'/newdisk/root/lang.log','w')
f1.truncate()

for i in f:
    m = re.findall(r'"size":([1-9]+).*"http_referrer":"(http.*)", "domain"',i)
    if m:
        f1.write(str(m) + "\n")
f.close()
f1.close()

shell:
awk -F\' '{s[$4] += $2}END{ for(i in s){  print i, s[i]/1000000"M" } }' ../lang.log | sort -r -n -k2 |head -100
