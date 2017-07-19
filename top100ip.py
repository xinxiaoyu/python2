#!/usr/bin/env python

import re

f = open(r'D:\access_json.log','r')
n = []

for i in f:
    m = re.findall(r'x_forwarded_for":"(\d+\.\d+\.\d+\.\d+)',i)
    if m:
       n += m
f.close()

from collections import Counter

ip_counts = Counter(n)
top_100 = ip_counts.most_common(100)
    
import urllib
import time

url = "http://freeapi.ipip.net/"

for ip,num in top_100:
    time.sleep(5)
    data = urllib.urlopen(url + ip).read()
    print ip,num,data
