# _*_ encoding = utf-8 _*_

"""
功能：抓取贴吧上某个帖子楼主发的所有图片
步骤：
    1.点击某个帖子得到链接，eg：http://tieba.baidu.com/p/4603702381
    2.分析源码找到帖子的总页数：PageData.pager = {"cur_page":1,"total_page":6};
    3.在原始链接上加上？n(n为页数)
    4.楼主发的图片是这样的形式<img class="BDE_Image" src=
    "http://imgsrc.baidu.com/forum/w%3D580/sign=35ea17fbdfca7bcb7d7bc7278e086b3f/80ca2f2dd42a2834737f183353b5c9ea14cebf44.jpg"
"""

from urllib import request
import re


# 获取页面信息
def getWebContent(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1)"
    headers = {"User-Agent": user_agent}
    req = request.Request(url, headers=headers)
    with request.urlopen(req) as f:
        print("Status: ", f.status, f.reason)
        content = f.read().decode("utf-8")
    return content

def saveImgs(content):
    patternCount = re.compile(r'PageData.pager = {"cur_page":\d,"total_page":(\d)}')
    pageCounts = re.findall(patternCount, content)
    pageCount = int(pageCounts[0])
    print("所有帖子页数：", pageCount)
    patternImg = re.compile(r'<img class="BDE_Image" src="(.*?)"')
    i = 1;
    while(i <= pageCount):
        pageUrl = url + '?' + str(i)
        print("第%d页的链接为：%s" % (i, pageUrl))
        count = 0
        pageContent = getWebContent(pageUrl)
        items = re.findall(patternImg, pageContent)
        for item in items:
            count += 1
            print(item)
            request.urlretrieve(item, "%s.jpg" % (str(i*10 + count)))
        i += 1

url = input("输入帖子链接：")
content = getWebContent(url)
saveImgs(content)
