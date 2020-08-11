'''

Author: TyrantLucifer
Function: Upload image to github in Typora
Time: 2020-08-10
Args: python(python3) upload.py Files1 Files2 ...

'''

# import package
import requests
import json
import base64
import os
import sys
import time

requests.adapters.DEFAULT_RETRIES = 5

# setting github username
USER = ""
# setting github repository name
REPO = ""
# setting images path
PATH = ""
# setting token
TOKEN = ""
# setting cdn url prefix
PREFIX_URL = "https://cdn.jsdelivr.net/gh/{0}/{1}/{2}/".format(
    USER,
    REPO,
    PATH
)
# setting api url
API_URL = "https://api.github.com/repos/{0}/{1}/contents/{2}/".format(
    USER,
    REPO,
    PATH
)
# setting http request headers
HEADERS = {
    "Authorization":"token " + TOKEN,
    "Accept":"application/vnd.github.v3+json",
    "Connection":'close'
}

# upload image to github
def uploadImg(filepath):
    if sys.platform.find("win") >= 0:
        filename = filepath.split("\\")[-1]
    else:
        filename = filepath.split("/")[-1]
    filename = generateFlieName(filename)
    with open(filepath, "rb") as file:
        content = file.read()
    content = base64.b64encode(content)
    content = str(content, 'utf-8')
    url = generateApiUrl(filename)
    commit = generateCommitMess(filename)
    data = {
        "message":commit,
        "content":content
    }
    data = json.dumps(data)
    result = requests.put(url, headers=HEADERS, data=data)
    result.close()
    return os.path.join(PREFIX_URL, filename)

# generate new file name by current time
def generateFlieName(filename):
    postfix = filename.split(".")[-1]
    prefix = time.strftime('%Y%m%d%H%M%S')
    filename = prefix + '.' + postfix
    return filename

# generate api url use filename
def generateApiUrl(filename):
    return os.path.join(API_URL, filename)

# generate commit message use filename
def generateCommitMess(filename):
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return currentTime + " " + "COMMIT" + " " + filename

# main function
def main():
    print("Upload Success:")
    for i in range(1, len(sys.argv)):
        if sys.argv[i]:
            print(uploadImg(sys.argv[i]))

if __name__ == "__main__":
    main()
