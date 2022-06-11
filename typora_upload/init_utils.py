"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: init_utils.py
@time: 2021/2/18 10:31
@desc: 初始化工具类集合
"""

import os
import sys
import platform
import configparser


class InitConfig(object):
    """初始化工具类

    当typora-upload启动时初始化相关属性

    属性:
        version: 版本号
        platform: 操作系统平台
        system: 操作系统
        home_dir: 家目录路径
        config_dir: 配置目录路径
        config_file: 配置文件
        config_lock_file: 配置锁文件
        log_file: typora-upload日志记录文件
    """

    def __init__(self):
        self.version = '1.0.0'
        self.platform = sys.platform
        self.system = platform.uname().version
        self.home_dir = os.path.expanduser('~')
        self.config_dir = os.path.join(self.home_dir,
                                       '.typora-upload')
        self.config_file = os.path.join(self.config_dir,
                                        'config.ini')
        self.config_lock_file = os.path.join(self.config_dir,
                                             '.config.lock')
        self.log_file = os.path.join(self.config_dir,
                                     'typora-upload.log')
        if not self.__is_exist_config_dir():
            self.__create_config_dir()

    def __is_exist_config_dir(self):
        if os.path.exists(self.config_dir):
            return True
        else:
            return False

    def __init_config_file(self):
        config = configparser.ConfigParser()
        config.add_section('default')
        config.set('default', 'storage', 'oss')
        config.add_section('github')
        config.add_section('oss')
        with open(self.config_file, 'w+') as file:
            config.write(file)
        with open(self.config_lock_file, 'w') as lock_file:
            lock_file.write('')

    def __create_config_dir(self):
        os.mkdir(self.config_dir)
        with open(self.config_file, 'w') as file:
            file.write('')
        self.__init_config_file()
