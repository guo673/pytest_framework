#!/usr/bin/python
# -*- encoding: utf-8 -*-

import logging
import time
import os
from logging.handlers import TimedRotatingFileHandler

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义日志文件路径
file_name = os.path.join(BASE_DIR, 'log',f'{time.strftime("%Y%m%d")}.log')

# 设置日志输出格式
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(message)s'
formatter = logging.Formatter(fmt)
# 创建一个文件日志输出和一个控制台日志输出
handler_file = logging.FileHandler(file_name)
handler_file.setFormatter(formatter)
handler_file.setLevel(logging.WARNING)
# handler_file.TimedRotatingFileHandler(filename=file_name,when="D",backupCount=7,encoding='utf-8')
handler_console = logging.StreamHandler()
handler_console.setFormatter(formatter)
handler_console.setLevel(logging.INFO)
# 创建一个名字为filename的logger对象
logger = logging.getLogger('myloger')
logger.setLevel(logging.INFO)
logger.addHandler(handler_file)
logger.addHandler(handler_console)

# 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

if __name__ == '__main__':
    print(file_name)
