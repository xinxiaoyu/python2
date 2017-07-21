#-*- coding:utf-8 -*-
import re

f = open(r'/newdisk/root/access_json.log1','r')
n = []

for i in f:
    m = re.findall(r'x_forwarded_for":"(\d+\.\d+\.\d+\.\d+)',i)
    if m:
       n += m
f.close()

from collections import Counter

ip_counts = Counter(n)
top_100 = ip_counts.most_common(5)    

import urllib
import time

url = "http://freeapi.ipip.net/"
f1 = open(r'/newdisk/root/access_json_log','w')
f1.truncate()
for ip,num in top_100:
    time.sleep(5)
    data = urllib.urlopen(url + ip).read()
    f1.write(str(num) + " " + data + "\n")

f1.close()

import subprocess

subprocess.Popen(["bash","/newdisk/root/awk.sh"])
f2 = open(r'/newdisk/root/access_json_log1','r')
x = []
y = []
for j in f2:
    x.append(j.split()[0])
    y.append(int(j.split()[1])) 

f2.close()
from pyecharts import Bar

bar = Bar("城市访问明细", "省份与访问量")
bar.add("城市访问量", x, y)
bar.show_config()
bar.render()

shell:
    awk -F\" '{print $1,$4}' /newdisk/root/access_json_log |awk '{print $1,$3}' | awk '{s[$2] += $1}END{ for(i in s){  print i, s[i]} }'
