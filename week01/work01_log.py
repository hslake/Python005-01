# -*- coding: utf-8 -*

import os
import logging
import time,datetime

def logFunc():
    nowDate = datetime.datetime.now().strftime("%Y%m%d")
    logDir = "/var/log/python-" + nowDate
    if not os.path.isdir(logDir):
        os.makedirs(logDir)
    logging.basicConfig(level=logging.INFO,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',filename=logDir + "/app.log")
    logging.info('geektime homework01')

if __name__ == "__main__":
    logFunc()
