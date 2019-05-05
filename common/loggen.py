import logging
import os
import time
class LogGen(object):
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        logtime = time.strftime('%Y%m%d%H%M',time.localtime())
        logname = os.path.dirname(os.path.abspath('.'))+'/logs/'+logtime+'.log'

        fileh = logging.FileHandler(logname)
        fileh.setLevel(logging.INFO)
        consoleh=logging.StreamHandler()
        consoleh.setLevel(logging.INFO)
        formatter = logging.Formatter\
            ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileh.setFormatter(formatter)
        consoleh.setFormatter(formatter)
        self.logger.addHandler(fileh)
        self.logger.addHandler(consoleh)
        #logger.info('hello,case pass')
    def getlog(self):
        return self.logger