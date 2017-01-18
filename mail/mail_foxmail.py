# -*- coding: utf-8 -*-
from smtplib import SMTP_SSL
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from datetime import date, timedelta
import os
import smtplib

# me == my email address
# you == recipient's email address
me = "a@qq.com"
you = "a@chinazyjr.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you
smtp_server = 'smtp.qq.com'
from_addr = 'a@qq.com'
password = 'a'

yesterday = (date.today() - timedelta(1)).strftime('%Y%m%d')
hkname = 'a' + yesterday + 'a.xlsx'
hkpath = 'C:\Users\a\PycharmProjects\python-bb\\'


part = MIMEBase('application', "octet-stream")
part.set_payload(open(hkpath + hkname, "rb").read())
part.add_header('Content-Disposition', 'attachment',filename=hkpath + hkname)
encoders.encode_base64(part)
msg.attach(part)

server = smtplib.SMTP(smtp_server, '587')
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_addr, password)
server.sendmail(me, you, msg.as_string())
server.quit()
