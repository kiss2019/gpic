from bs4 import BeautifulSoup
import requests
import os
import re
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    # 'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    # 'Accept-Encoding': 'gzip',
    # "Referer": "http://www.baidu.com/"
}   #头部文件
data=''
url = 'http://www.baidu.com'

#把文件保存在C:\pycode\jpg目录下
def savePath():
    # path="jpg" #jpg为保存目录，可随意更改
    path= r"C:\pycode\jpg"
    #如果不存在，新建一个
    if not os.path.exists(path):
          os.makedirs(path)
    os.chdir(path) #进入当前目录
    print(os.getcwd()) #得到当前目录
#获取网页内容
def getHTMLText(url):
    global data
    try:
        r = requests.get(url, headers=headers, timeout=20)
        r.raise_for_status()
        print(r.status_code)
        r.encoding = r.apparent_encoding
        data = r.content.decode('utf-8')
        # data = r.text
        #         print(data) 打印时不会有\r\n

        return data  # 返回值时有\r\n
    except:
        return "产生异常"


# getHTMLText(url)

# with open('03ssl.html', 'w',encoding='utf-8') as f:
#     f.write(data)
savePath()
url='http://news.baidu.com'
r = requests.get(url, headers=headers, timeout=20)
r.raise_for_status()
r.encoding = r.apparent_encoding
data = r.content.decode('utf-8')


