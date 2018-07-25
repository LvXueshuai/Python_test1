'''

import logging

logging.basicConfig(    #常用方式
    level=logging.DEBUG,
    filename="logger.log",
    #filemode='a',
    format="%(asctime)s %(filename)s %(lineno)d %(message)s"

)

logging.debug("debug")
logging.info("info")
logging.warning("warring")
logging.error("erro")
logging.critical("critical")
'''

import logging

logger = logging.getLogger()   #定义对象方式

fh = logging.FileHandler('test_log')    #向文件发送日志内容
ch = logging.StreamHandler()  #向屏幕发送日志内容

fm = logging.Formatter("%(asctime)s %(filename)s %(lineno)d %(message)s")

fh.setFormatter(fm)
ch.setFormatter(fm)

logger.addHandler(fh)
logger.addHandler(ch)
logger.setLevel('DEBUG')   #设置优先级
#--------------------------

logging.debug("debug")
logging.info("info")
logging.warning("warring")
logging.error("erro")
logging.critical("critical")
