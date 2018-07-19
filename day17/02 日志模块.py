# import logging
# 进行基本的日志配置
# logging.basicConfig(filename='access.log',
#                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',
#                     level=10,
#                     # stream=True
#                     )

# 日志级别遵循原则：自下而上进行匹配 #debug-》info-》warning-》error-》critical
# logging.debug('调试信息') #10
# logging.info('正常信息') #20
# logging.warning('不好啦着火啦') #30
# logging.error('报错信息') #40
# logging.critical('严重错误信息') #50

# 问题：
#1、没有指定日志级别
#2、没有指定日志格式
#3、只能往屏幕打印，没有写入文件


# 新问题
#1、不能指定字符串编码
#2、只能往文件中打印


import logging
# logging模块包含四种角色：logger，filter，formatter，handler
#1、logger：负责产生日志信息
logger1=logging.getLogger('交易日志')
# logger2=logging.getLogger('用户相关')

#2、filter：负责筛选日志

#3、formatter：控制日志输出格式
formatter1=logging.Formatter(
    fmt='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %X'
)
formatter2=logging.Formatter(
    fmt='%(asctime)s:%(message)s',
    datefmt='%Y-%m-%d %X'
)


#4、handler：负责日志输出的目标
h1=logging.FileHandler(filename='a1.log',encoding='utf-8')
h2=logging.FileHandler(filename='a2.log',encoding='utf-8')
sm=logging.StreamHandler()


#5、绑定logger对象与handler对象
logger1.addHandler(h1)
logger1.addHandler(h2)
logger1.addHandler(sm)

#6、绑定handler对象与formatter对象
h1.setFormatter(formatter1)
h2.setFormatter(formatter1)
sm.setFormatter(formatter2)

#7、设置日志级别：可以在两个关卡进行设置logger与handler
logger1.setLevel(10)
h1.setLevel(10)
h2.setLevel(10)
sm.setLevel(10)




logger1.info('Egon借给李杰100W')



