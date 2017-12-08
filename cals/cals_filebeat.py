#!/usr/bin/env python3.5
# coding=utf-8

import logger

def cals(log,redis_db):
       message_str = eval(log)['message']
       message_list = message_str.split(' ')
       server = message_list[3]
       access_result = message_list[13]
       datastr = message_list[8].split('T')[0].replace('-','')
       try:
           channel = message_list[11].split('/')[4].split('?')[0]
           ip = message_list[5]
           ip_key = 'fb:' + server + ':' + datastr + ':IP'
           channel_key = 'fb:' + server + ':' + datastr + ':channel'
           #print(server,access_result,datastr,key)
           redis_db.set_value(ip_key,ip)
           redis_db.set_value(channel_key,channel)
       except IndexError:
           print(message_str)
           logger.logger.warning("filebeat Wrong logger Format: " + message_str)
