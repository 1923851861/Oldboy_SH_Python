import logging.config
from dir1.dir2 import settings

logging.config.dictConfig(settings.LOGGING_DIC)

# logger1=logging.getLogger('用户相关') #name='用户相关'
# logger2=logging.getLogger('交易日志') #name='交易日志'
logger3=logging.getLogger('egon') #name='交易日志'

# logger1.info('xxx登陆成功')
# logger2.info('Egon给李杰转账100块')
logger3.info('egon。。。。。。。。。。。。')




















# try:
#     print(1)
#     print(2)
#     print(3)
#     xxxxx
# except NameError as e: # e="name 'xxxxx' is not defined"
#     logger1.error(e)
#
#
# print(4)
# print(5)
# print(6)
