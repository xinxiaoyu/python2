#!/usr/bin/python
#-*- coding: utf-8 -*-
import paramiko
import getpass
import sys

paramiko.util.log_to_file('/scripts/paramiko.log') 

passwd = getpass.getpass('Input passwd: ')
cmd = sys.argv[1]

def ssh(ip, username, passwd, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        for line in stdout:
            print line.strip('\n')
        print '%s OK\n' %(ip)
        print '-------------------------------------------------'
        ssh.close()
    except :
        print '%s Error\n' %(ip)

with open(r'/home/langyaofeng/scripts/hosts', 'r') as f:
    for i in f:
        m = i.replace('\n', '')
        ssh(m, "root", passwd, cmd)
