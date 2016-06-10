# encoding = utf-8
# 功能:抓取糗事百科的内容

from urllib import request
import re

url = input("输入糗事百科链接: ")
user_agent = "Mozilla/5.0 (Windows NT 6.1)"
headers = {"User-Agent": user_agent}  # 请求头
req = request.Request(url, headers=headers)
with request.urlopen(req) as f:
    print("Status: ", f.status, f.reason)
    content = f.read().decode("utf-8")
    pattern = re.compile(r'<div.*?author clearfix">.*?title="(.*?)">.*?content">(.*?)</div>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print(item[0], ':', item[1])
