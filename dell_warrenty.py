#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-2-15
# @Version : v2.0

try:  
    from lxml import html
except ImportError:  
    raise SystemExit("no lxml module, please install with pip!")

import urllib2

headers = {  
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, li
ke Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Cookie': ''
}


def ServiceCode(sc):  
    sc_url = 'http://www.dell.com/support/home/cn/zh/cnbsd1/product-support/serv
icetag/%s/warranty' % sc
    result_file = open('results.txt', 'ab+')
    try:
        req = urllib2.Request(sc_url, headers=headers)
        res = urllib2.urlopen(req, timeout=30).read().decode('utf-8')
    except Exception as e:
        raise e
    else:
        ll = html.fromstring(res)
        tags = ll.xpath('//span[@class="not-bold"]/text()')
        stoptime = ll.xpath('//table[2]/tbody/tr/td[3]/text()')[-1]
        stag = tags[0]
        sdeliver = tags[1]
        print u'%s   %s    %-10s\n' % (stag, sdeliver, stoptime)
        towrite = u'%s  %s   %-10s\n' % (stag, sdeliver, stoptime)
    result_file.write(towrite.encode('utf-8') + '\n')
    result_file.close()

import time

def ReadCode(sfile):  
    with open(sfile) as sfiles:
        lines = sfiles.readlines()
        for line in lines:
            ServiceCode(line.strip())
            time.sleep(5)        

if __name__ == '__main__':  
    scfile = '730'
    ReadCode(scfile)
