#!/usr/bin/env python
#create at 20170707

import re

f = open(r'/root/access_json.log1','r')
n = []

for i in f:
    m = re.findall(r'domain":"(\w+\.\w+\.\w+)".*status":(\d+)',i)
    n += m
f.close()

p = set(n)
for item in p:
    print item,n.count(item)
