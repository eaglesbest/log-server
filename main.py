#!/usr/bin/env python3.5
# coding=utf-8

import config
from imp import reload
import importlib
import logger
import redis_op
import time

def main():
    logger.init_log('log-server')
    redis_db = redis_op.redisClass()
    while True:
        reload(config)
        for module in config.modules:
            if not redis_db.get_len(module):
                time.sleep(10)
                continue 
            try:
                module_func = config.modules[module]
                cals_module = "cals." + module_func
                cals_func = importlib.import_module(cals_module)
            except ImportError as e:
                logger.logger.error("There is no cals module %s" % cals_module)
                #print(e) 
                continue
            log = redis_db.get_one_log(module)
            cals_func.cals(log,redis_db)
            #print("Call cals_vdn")

if __name__ == '__main__':
    main()
