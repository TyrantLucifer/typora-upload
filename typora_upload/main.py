"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: main.py
@time: 2021/2/18 21:36
@desc: typora-upload入口函数
"""

import argparse
from typora_upload.functions import *


def get_parser():
    parser = argparse.ArgumentParser(description=color.blue("The typora image upload plugin based Python."),
                                     epilog=color.yellow('Powered by ') + color.green('tyrantlucifer') + color.yellow(
                                         ". If you have any questions,you can send e-mails to ") + color.green(
                                         "tyrantlucifer@gmail.com"))
    parser.add_argument("-u", "--upload", metavar="file_path", help="upload image file")
    parser.add_argument("-s", "--storage", metavar="storage", help="storage type")
    parser.add_argument("-i", "--init", metavar="storage", help="init storage config")
    parser.add_argument("-v", "--version", action="store_true", help="display version")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.upload:
        Upload.upload(args.upload)
    elif args.init:
        if args.init == 'oss':
            InitStorgeConfig.init_oss()
        elif args.init == 'github':
            InitStorgeConfig.init_github()
    elif args.storage:
        InitStorgeConfig.update_storage(args.storage)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
