"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: upload_utils.py
@time: 2022/6/11 18:57
@desc:
"""

import json
import base64
import oss2
import re
import requests

from typora_upload.config_utils import *


class Common(object):

    def __init__(self):
        pass

    @staticmethod
    def is_http_url(path):
        if re.match(r'(http|https)://([\w.]+/?)\S*', path):
            return True
        else:
            return False

    @staticmethod
    def generate_file_name(file):
        postfix = file.split(".")[-1]
        prefix = time.strftime('%Y%m%d%H%M%S')
        filename = prefix + '.' + postfix
        return filename

    @staticmethod
    def get_http_file_content(path):
        result = requests.get(path)
        return result.content

    @staticmethod
    def get_local_file_content(path):
        with open(path, "rb") as file:
            content = file.read()
        return content


class OssUploader(object):

    def __init__(self):
        self.access_key_id = ConfigUtils.get_value('oss', 'access_key_id')
        self.access_key_secret = ConfigUtils.get_value('oss', 'access_key_secret')
        self.bucket_name = ConfigUtils.get_value('oss', 'bucket_name')
        self.endpoint = ConfigUtils.get_value('oss', 'endpoint')
        self.path_prefix = ConfigUtils.get_value('oss', 'path_prefix')
        self.domain_name = ConfigUtils.get_value('oss', 'domain_name')
        self.bucket = oss2.Bucket(oss2.Auth(self.access_key_id, self.access_key_secret), self.endpoint,
                                  self.bucket_name)

    def upload(self, path):
        if Common.is_http_url(path):
            filename = path.split("/")[-1]
            filename = Common.generate_file_name(filename)
            content = Common.get_http_file_content(path)
            self.bucket.put_object('{0}/{1}'.format(self.path_prefix, filename), content)
        else:
            if sys.platform.find("win") >= 0:
                filename = path.split("\\")[-1]
            else:
                filename = path.split("/")[-1]
            filename = Common.generate_file_name(filename)
            self.bucket.put_object_from_file('{0}/{1}'.format(self.path_prefix, filename), path)
        return 'https://{0}/{1}/{2}'.format(self.domain_name, self.path_prefix, filename)


class GithubUploader(object):

    def __init__(self):
        self.user = ConfigUtils.get_value('github', 'user')
        self.repo = ConfigUtils.get_value('github', 'repo')
        self.path_prefix = ConfigUtils.get_value('github', 'path_prefix')
        self.token = ConfigUtils.get_value('github', 'token')
        self.api_url = "https://api.github.com/repos/{0}/{1}/contents/{2}/".format(
            self.user,
            self.repo,
            self.path_prefix)
        self.prefix_url = "https://cdn.jsdelivr.net/gh/{0}/{1}/{2}/".format(
            self.user,
            self.repo,
            self.path_prefix
        )
        self.headers = {
            "Authorization": "token " + self.token,
            "Accept": "application/vnd.github.v3+json",
            "Connection": 'close'
        }

    def upload(self, path):
        if Common.is_http_url(path):
            filename = path.split("/")[-1]
            filename = Common.generate_file_name(filename)
            content = Common.get_http_file_content(path)
        else:
            if sys.platform.find("win") >= 0:
                filename = path.split("\\")[-1]
            else:
                filename = path.split("/")[-1]
            filename = Common.generate_file_name(filename)
            content = Common.get_local_file_content(path)
        content = base64.b64encode(content)
        content = str(content, 'utf-8')
        url = self.__generate_api_url(filename)
        commit = self.__generate_commit_message(filename)
        data = {
            "message": commit,
            "content": content
        }
        data = json.dumps(data)
        result = requests.put(url, headers=self.headers, data=data)
        result.close()
        return os.path.join(self.prefix_url, filename)

    def __generate_api_url(self, filename):
        return os.path.join(self.api_url, filename)

    def __generate_commit_message(self, filename):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time + " " + "COMMIT" + " " + filename
