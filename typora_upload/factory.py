"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: factory.py
@time: 2022/6/12 00:15
@desc: uploader工厂
"""

from typora_upload.upload_utils import *


class UploaderFactory(object):

    def __init__(self):
        pass

    @staticmethod
    def get_uploader(storage):
        if storage == 'oss':
            return OssUploader()
        elif storage == 'github':
            return GithubUploader()
