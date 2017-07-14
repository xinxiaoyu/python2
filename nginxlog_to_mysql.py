#!/usr/bin/env python

import re
import mysql.connector

cnx = mysql.connector.connect(user='', database='log',password='',host='192.168.1.126')
cursor = cnx.cursor()

f = open(r'/root/access_json.log','r')

for i in f:
    m = re.findall(r'timestamp":"(\d+-\d+-\d+T\d+:\d+:\d+).*domain":"(www\.qq\.com)".*status":(\d+).*x_forwarded_for":"(\d+\.\d+\.\d+\.\d+)',i)
    if m:
        for x,y,z,h in m:
            sql = 'insert nginxlog values("%s","%s","%s","%s")' % (x,y,z,h)
            cursor.execute(sql)
            cnx.commit()
f.close()
cursor.close()
cnx.close()
