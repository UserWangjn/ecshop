import logging
import os
import time

logger = logging.getLogger('LogTestFun')
logger.setLevel(logging.INFO)
logtime = time.strftime('%Y%m%d%H%M',time.localtime())
logpath = os.path.dirname(os.path.abspath('.'))+'/logs/'+logtime+'.log'

fileh = logging.FileHandler(logpath)
fileh.setLevel(logging.INFO)

formatter = logging.Formatter\
    ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileh.setFormatter(formatter)
logger.addHandler(fileh)

logger.info('hello,case pass')