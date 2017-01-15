# -*- coding: utf-8 -*-
from smtplib import SMTP_SSL
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from datetime import date, timedelta

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'mail@qq.com'
password = 'passwd'
to_addr =['mail@og.com']
cc = ['a.com','aa@gmail.com','aa@163.com']
smtp_server = 'smtp.qq.com'
to_addrs = [to_addr] + cc
msg = MIMEMultipart()
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
msg['From'] = _format_addr(u'aa <%s>' % from_addr)
msg['To'] = _format_addr(u'呵呵 <%s>' % to_addr)
msg['Subject'] = Header(u'呵呵', 'utf-8').encode()

yesterday = (date.today() - timedelta(1)).strftime('%Y%m%d')
hkname = 'FXD_' + yesterday + '_REPAYMENT.xlsx'
hkpath = 'C:\Usersa\PycharmProjects\python-bb\\'
with open(hkpath + hkname, 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEMultipart('mixed', 'xlsx', filename=hkname)
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=hkname)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, '587')
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_addr, password)
server.sendmail(from_addr, to_addrs,msg.as_string())
server.quit()

