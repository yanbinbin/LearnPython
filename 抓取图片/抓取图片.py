# _*_ coding: utf-8 _*_
# 功能: 爬取贴吧图片

from urllib import request
import re

# 定义一个函数,得到内容

def getWebContent(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1)"
    headers = {"User-Agent":user_agent}
    req = request.Request(url, headers=headers)
    with request.urlopen(req) as f:
        print("Status: ", f.status, f.reason)
        content = f.read().decode("utf-8")
        return content

def getImage(content):
    pattern = re.compile(r'src="(.*?)"')
    items = re.findall(pattern, content)
    print(items)
    count = 0
    for item in items:
        count += 1
        request.urlretrieve(item, "%s.jpg" % count)

u = input("请输入链接: ")
con = getWebContent(u)
getImage(con)
