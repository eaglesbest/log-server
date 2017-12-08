#!/usr/bin/env python3.5
#coding:utf-8

import redis

class redisClass(object):
    def __init__(self,host='127.0.0.1',port=6379):
        self.conn = redis.StrictRedis(host=host,port=port,db=0)
    
    def get_one_log(self,key):
        value = self.conn.lpop(key).decode()
        return value 
   
    def set_value(self,key,member,increment=1):
        self.conn.zincrby(key,member,increment)       

    def get_len(self,key):
        if self.conn.type(key).decode() == 'list':
            return self.conn.llen(key)
        return self.conn.zcard(key)  

if __name__ == '__main__':
    redis_db = redisClass()
    while True:
        if not redis_db.get_len('test'):
            break
        log_filebeat = redis_db.get_value('test')
        #print(log_filebeat)
        message_str = eval(log_filebeat)['message']
        message_list = message_str.split(' ')
        server = message_list[5]
        access_result = message_list[13]
        datastr = message_list[8].split('T')[0]
        channel = message_list[11].split('/')[4].split('?')[0]
        ip = message_list[5]
        ip_key = 'VDN:' + server + ':' + datastr + ':IP'
        channel_key = 'VDN:' + server + ':' + datastr + ':' + channel 
        #print(server,access_result,datastr,key)
        redis_db.set_value(ip_key,ip)
        redis_db.set_value(channel_key,channel)
