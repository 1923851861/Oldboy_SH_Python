"""
logging配置
"""
import os
import logging.config

# 定义三种日志输出格式 开始
standard_format = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'

simple_format = '%(asctime)s - %(levelname)s - %(message)s'

id_simple_format = '[%(asctime)s] %(message)s'


# log文件的全路径
logfile1_path = r'D:\SH_fullstack_s2\day17\a1.log'
logfile2_path = r'D:\SH_fullstack_s2\day17\a2.log'

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

    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        'logger1': {
            'handlers': ['h1','h2','sm'],
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
    },
}


























