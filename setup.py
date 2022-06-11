import codecs
from setuptools import setup

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="typora-upload",
    version="1.0.0",
    author="tyrantlucifer",
    author_email="tyrantlucifer@gmail.com",
    description="The typora image upload plugin based Python.",
    url="https://github.com/tyrantlucifer/typora-upload",
    packages=[
        "typora_upload"
    ],
    entry_points={
        'console_scripts': [
            'typora-upload = typora_upload.main:main'
        ]
    },
    install_requires=[
        "requests",
        "qrcode",
        "colorama",
        "oss2"
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)
