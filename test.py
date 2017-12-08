#!/usr/bin/env python3.5
#coding:utf-8

# logstr = 'Nov 16 20:49:14 bj-vp ses-server: 127.0.0.1 - - 2017-11-16T20:49:14+0800 0 "GET http://127.0.0.1/live/livechina-wuzhen?fmt=x264_1000K_ts&cpid=_admin&size=1280X720 HTTP/1.1" 500 407 "http://www.streamocean.com/chnl-cache" "-" -'
# 
# loglist = logstr.split(' ')
# #print(loglist)
# server = loglist[5]
# access_result = loglist[13]
# datastr = loglist[8].split('T')[0]
# key = 'VDN:' + server + ':' + datastr + ':IP'
# 
# print(server,access_result,datastr,key)

import config
from imp import reload
import time

while True:
    reload(config)
    for module in config.modules:
        print(module,config.modules[module])
        time.sleep(5)
