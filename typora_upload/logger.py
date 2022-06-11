"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: logger.py
@time: 2021/2/18 19:59
@desc: 初始化全局log变量
"""

import logging
import time

from typora_upload.init_utils import *
from typora_upload.print_utils import *

# 初始化工具类init_utils.InitConfig
init_config = InitConfig()

# 初始化打印工具类
color = Colored()

# 初始化全局logger记录格式及级别
logger = logging.getLogger("typora-upload")
logger.setLevel(logging.INFO)

# 初始化全局logger记录格式
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - [%(funcName)s] - %(levelname)s: %('
                              'message)s')

# 初始化全局logger文件记录格式及级别
log_file_handler = logging.FileHandler(init_config.log_file)
log_file_handler.setLevel(logging.INFO)
log_file_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)


# 定义计算函数运行时间装饰器
def calculate(func):
    def main(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        logger.info("Func - {0} Total time: {1}s".format(func.__name__,
                                                         round(time.time() - start, 2)))
    return main
