#!/usr/bin/env python3.5
# coding=utf-8

# modules的键值是指要进行日志处理的产品名称，如VDN、LR、MSM等
# 同时该键值也是在redis数据库存储的键值
# modules的value值是处理该日志的程序名称

modules = {
           'filebeat':'cals_filebeat',
           'vdn':'cals_vdn',
          }
