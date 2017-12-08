#!/usr/bin/env python3.5
# coding=utf-8

import logging

logger = None
log_dir = 'logs/'

def init_log(name):
    # logging.basicConfig(level=logging.warning,
    #                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                 datefmt='%a, %d %b %Y %H:%M:%S',
    #                 filename='logs/log',
    #                 filemode='w')
    global logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.WARNING)
    fh = logging.FileHandler(log_dir + name + ".log")
    formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s","%a, %d %b %Y %H:%M:%S")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
