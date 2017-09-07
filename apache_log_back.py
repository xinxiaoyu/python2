#!/usr/bin/env pytho
#python2.7

import os
import shutil
from datetime import date,timedelta

today_time=date.today()
http_log_path='/var/log/httpd/'

for dirpath,dirnames,filenames in os.walk(http_log_path):
    for filename in filenames:
        if filename.endswith('log'):
            if not os.path.isfile(http_log_path+filename+str(today_time)):
                shutil.copy(http_log_path+filename,http_log_path+filename+str(today_time))
                open(http_log_path+filename,'w').close()
            else:
                print '%s is aready exist!' % (http_log_path+filename+str(today_time))
