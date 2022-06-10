'''

Author: TyrantLucifer
Function: Upload image to github in Typora
Time: 2022-01-24
Args: python(python3) upload.py Files1 Files2 ...

'''

# import package
import os
import sys
import time
import oss2

access_key_id = ''
access_key_secret = ''
bucket_name = ''
endpoint = ''
path_prefix = 'images'
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

# upload image to github
def uploadImg(filepath):
    if re.match(r'(http|https):\/\/([\w.]+\/?)\S*', filepath):
        filename = filepath.split("/")[-1]
        result = requests.get(filepath)
        filename = generateFlieName(filename)
        bucket.put_object('{0}/{1}'.format(path_prefix, filename), result.content)
    else:
        if sys.platform.find("win") >= 0:
            filename = filepath.split("\\")[-1]
        else:
            filename = filepath.split("/")[-1]
        filename = generateFlieName(filename)
        bucket.put_object_from_file('{0}/{1}'.format(path_prefix, filename), filepath)
    return 'https://{0}/{1}/{2}'.format(domain_name, path_prefix, filename)

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
