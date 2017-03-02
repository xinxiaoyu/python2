# -*- coding:utf-8 -*-

import os.path
from datetime import date,timedelta
import shutil

todayfile = date.today().strftime('%Y-%m-%d')
todayfile1 = date.today().strftime('%Y%m%d')
src = r"E:\RedMineBak\50.118\DCBack_%s.rar" % todayfile
src1 = r"E:\RedMineBak\Exchange\Exchange_%s.rar" % todayfile
src2 = r"E:\RedMineBak\RedMine\RedMine_%s.rar" % todayfile
src3 = r"E:\RedMineBak\Orcl\orcl%s.dmp" % todayfile1

dst = r"F:\RedMineBak\50.118\DCBack_%s.rar" % todayfile
dst1 = r"F:\RedMineBak\Exchange\Exchange_%s.rar" % todayfile
dst2 = r"F:\RedMineBak\RedMine\RedMine_%s.rar" % todayfile
dst3 = r"F:\RedMineBak\Orcl\orcl%s.dmp" % todayfile1

if os.path.isfile(src):
    shutil.copy(src,dst)
else:
    pass

if os.path.isfile(src1):
    shutil.copy(src1,dst1)
else:
    pass

if os.path.isfile(src2):
    shutil.copy(src2,dst2)
else:
    pass

if os.path.isfile(src3):
    shutil.copy(src3,dst3)
else:
    pass
