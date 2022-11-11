import os
import re

import requests as requests
from pip._internal.network import session


# 根据之前爬取到的用户Id得到每个用户的相册主页，得到每个用户拥有的相册id：
def find_albumId(Id, savepath=None):
    album_url = 'http://photo.renren.com/photo/{0}/albumlist/v7?offset=0&limit=40#'.format(Id)
    try:
        r = session.get(album_url, timeout=5, proxies=proxy, headers=headers)
        Idpath = savepath + Id + "/"
    except Exception as e:
        print(e)
        r = session.get(album_url, timeout=5, proxies=proxy, headers=headers)
    try:
        x = re.findall('"albumId":"(.*?)"', str(r.text))
    except Exception as e:
        print(e)
    return (x, Idpath)


# 根据相册Id找到每个相册下的图片id，从而获取到图片
def find_picId(Id, albumId):
    pic_url = r'http://photo.renren.com/photo/{0}/album-{1}/v7'.format(Id, albumId[i])
    # print(pic_url)
    try:
        r2 = session.get(pic_url, timeout=5, proxies=proxy, headers=headers)
    except Exception as e:
        print(e)
        r2 = session.get(pic_url, timeout=5, proxies=proxy, headers=headers)
    try:
        y = re.findall('"url":"(.*?)"', str(r2.text))
    except Exception as e:
        print(e)
    return y


# 模拟登陆

proxy = {
    '194.233.73.105',
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}
session = requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email": "bxzhutianyu@126.com", "password": "CMZ19962011"}
session.post(post_url, data=post_data, proxies=None, headers=headers)

# 存储图片到本地
namelist = './all'
f1 = open(namelist, 'r')
lines = f1.readlines()
for line in lines:
    Id = line.strip('\n')
    albumId, Idpath = find_albumId(Id)
    num = 0
    if albumId:
        if not os.path.exists(Idpath):
            os.makedirs(Idpath)
        for i in range(len(albumId)):
            y = find_picId(Id, albumId)
            for j in range(len(y)):
                picpath = Idpath + Id + '_' + str(num) + '.jpg'
                with open(picpath, "wb") as f:
                    try:
                        Url = '/'.join(y[j].split('\/'))
                        print(Url)
                        picture = requests.get(Url, proxies=proxy, timeout=5, headers=headers)
                        f.write(picture.content)
                    except Exception as e:
                        print(e)
                        continue
                print("%s下载成功" % picpath)
                num += 1
        # 针对1017空的特殊处理，后面可删除
        if not os.listdir(Idpath):
            os.rmdir(Idpath)
print("all done")
