"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: config_utils.py
@time: 2021/2/18 22:42
@desc:
"""

from typora_upload.logger import *


class ConfigUtils(object):
    """配置项工具类

    提供从本地配置文件中读取对应参数的功能

    属性:
        config: 配置文件对象
    """
    config = configparser.ConfigParser()
    config.read(init_config.config_file)

    def __init__(self):
        pass

    @staticmethod
    def get_value(section, key):
        return ConfigUtils.config.get(section, key)

    @staticmethod
    def set_value(section, key, value):
        ConfigUtils.config.set(section, key, str(value))
        with open(init_config.config_file, 'w+') as file:
            ConfigUtils.config.write(file)

