#-*- coding:utf-8 -*-
#python2.7

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.base import MIMEBase
from email import encoders

def send_mail(from_addr, password,to_addr, subject='testMail', content='This is a test mail!', file='/tmp/aureport2.txt'):
    msg = MIMEMultipart()
    msg.attach(MIMEText(content, 'plain', 'utf-8'))
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg['From'] = u'%s <%s>' % (from_addr,from_addr)
    msg['To'] = u'<%s>' % to_addr

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file, "rb").read())
    part.add_header('Content-Disposition', 'attachment',filename=file)
    encoders.encode_base64(part)
    msg.attach(part)

    server = smtplib.SMTP('smtp.exmail.qq.com','587')
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
