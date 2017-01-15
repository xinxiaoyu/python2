from __future__ import print_function

from decimal import Decimal
from datetime import datetime, date, timedelta

import mysql.connector
import  xlsxwriter

cnx = mysql.connector.connect(user='a', database='a',password='a',host='a')
cursor = cnx.cursor()

query = ("select a,b,c from a")
cursor.execute(query)

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0


for item,item2,item3 in cursor:
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, item2)
    worksheet.write_number(row, col + 2, int(item3))
    row += 1

cursor.close()
cnx.close()
workbook.close()
