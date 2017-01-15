# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'myaddress'
password = 'passwd'
to_addr = 'youaddress'
smtp_server = 'IP or host'

msg = MIMEMultipart()
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
msg['From'] = _format_addr(u'呵呵 <%s>' % from_addr)
msg['To'] = _format_addr(u'呵呵 <%s>' % to_addr)
msg['Subject'] = Header(u'报表', 'utf-8').encode()

with open('C:\Users\a\PycharmProjects\python-bb\demo.xlsx', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEMultipart('mixed', 'xlsx', filename='demo.xlsx')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='demo.xlsx')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
