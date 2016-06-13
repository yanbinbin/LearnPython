'''
登录

对于需要用户登录的网站信息的爬取

'''

# _*_ coding=utf-8 _*_

import urllib.request, gzip, re, http.cookiejar, urllib.parse
import sys


# 解压缩函数
def ungzip(data):
    try:
        print("正在解压缩...")
        data = gzip.decompress(data)
        print("解压完成")
    except:
        print("未经解压, 无需解压...")
    return data


# 构造文件头
def getOpener(header):
    # 设置一个cookie处理器, 它负责从服务器下载cookie到本地, 并且在发送请求时带上本地的cookie
    cookie_jar = http.cookiejar.CookieJar()
    cp = urllib.request.HTTPCookieProcessor(cookie_jar)
    opener = urllib.request.build_opener(cp)
    headers = []
    for key, value in header.items():
        elem = (key,value)
        headers.append(elem)
    opener.addheaders = headers
    return opener

# 获取_xsrf
def getXsrf(data):
    cer = re.compile(r'name="_xsrf" value="(.*?)"', flags=0)
    str = cer.findall(data)
    print("_xsrf = ", str[0])
    return str[0]


# 根据网站报头信息设置headers
headers = {
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate,br',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}

url = "https://www.zhihu.com/"
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)

# 获取知乎首页内容, 获取_xsrf
data = res.read()
data = ungzip(data)
_xsrf = getXsrf(data.decode('utf-8'))

opener = getOpener(headers)
# post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
url+='login/email'
name='424410522@qq.com'
passwd='bin19930421'

# 分析构造post数据
postDict={
    '_xsrf':_xsrf,
    'email':name,
    'password':passwd,
    'remember_me':'true'
}

# 给post数据编码
postData = urllib.parse.urlencode(postDict).encode()

# 构造请求
res = opener.open(url, postData)
data = res.read()
# 解压缩
data = ungzip(data)
print("请求结果: ", data.decode())
