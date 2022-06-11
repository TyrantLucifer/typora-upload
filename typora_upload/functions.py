"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: functions.py
@time: 2022/6/11 19:35
@desc:
"""

from typora_upload.factory import *


class Upload(object):

    def __init__(self):
        pass

    @staticmethod
    def upload(path):
        storage = ConfigUtils.get_value('default', 'storage')
        uploader = UploaderFactory.get_uploader(storage)
        image_url = uploader.upload(path)
        print("Upload Success:")
        print(image_url)


class InitStorgeConfig(object):

    def __init__(self):
        pass

    @staticmethod
    def init_oss():
        access_key_id = input("access_key_id:")
        ConfigUtils.set_value('oss', "access_key_id", access_key_id)
        access_key_secret = input("access_key_secret:")
        ConfigUtils.set_value('oss', "access_key_secret", access_key_secret)
        bucket_name = input("bucket_name:")
        ConfigUtils.set_value('oss', "bucket_name", bucket_name)
        endpoint = input("endpoint:")
        ConfigUtils.set_value('oss', "endpoint", endpoint)
        path_prefix = input("path_prefix:")
        ConfigUtils.set_value('oss', "path_prefix", path_prefix)
        domain_name = input("domain_name:")
        ConfigUtils.set_value('oss', "domain_name", domain_name)

    @staticmethod
    def init_github():
        user = input("user:")
        ConfigUtils.set_value('github', 'user', user)
        repo = input("repo:")
        ConfigUtils.set_value('github', 'repo', repo)
        path_prefix = input("path_prefix:")
        ConfigUtils.set_value('github', 'path_prefix', path_prefix)
        token = input("token:")
        ConfigUtils.set_value('github', 'token', token)

    @staticmethod
    def update_storage(storage):
        ConfigUtils.set_value('default', 'storage',storage)