#!/usr/bin/env python

import re
from pyecharts import Pie
from datetime import date, timedelta

yesterday = (date.today() - timedelta(1)).strftime('%Y%m%d')

f = open(r'/root/access_json.log1','r')
n = []

for i in f:
    m = re.findall(r'status":(\d+)',i)
    n += m
f.close()

x = []
y = []

p = set(n)
for item in p:
    x.append(item)
    y.append(n.count(item))

pie = Pie("http_status")
pie.add("", x, y, is_label_show=True)
pie.show_config()
pie.render('/var/www/html/' + yesterday + '.html')
