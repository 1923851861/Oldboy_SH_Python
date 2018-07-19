"""
logging配置
"""
import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))


# 定义三种日志输出格式 开始
standard_format = '%(asctime)s - %(filename)s:%(lineno)d - %(name)s - %(levelname)s - %(message)s'

simple_format = '%(asctime)s - %(levelname)s - %(message)s'

id_simple_format = '[%(asctime)s] %(message)s'


# log文件的全路径
logfile1_path = os.path.join(BASE_DIR,'a1.log')
logfile2_path = os.path.join(BASE_DIR,'a2.log')
logfile3_path = os.path.join(BASE_DIR,'a3.log')

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'formatter1': {
            'format': standard_format
        },
        'formatter2': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'sm': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'formatter2'
        },
        #打印到文件的日志,收集info及以上的日志
        'h1': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'formatter1',
            'filename': logfile1_path,  # 日志文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'h2': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'formatter1',
            'filename': logfile2_path,  # 日志文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'h3': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'formatter1',
            'filename': logfile3_path,  # 日志文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },

    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['h1','h2','sm'],
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
        'egon':{
            'handlers': ['h3',],
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
    },
}
























