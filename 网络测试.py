from bs4 import BeautifulSoup
import requests
import os
import  re
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Accept-Encoding': 'gzip',
    "Referer": "http://finance.sina.com.cn/"
}   #头部文件
# path="jpg" #jpg为保存目录，可随意更改
path= r"C:\Users\1\jpg"
os.chdir(path)
url = 'http://finance.sina.com.cn/zt_d/weekly356/'
response = requests.get(url, headers=headers)
response.encoding='utf-8'

html_soup = BeautifulSoup(response.text, 'lxml')
print(type(html_soup))
all_url=html_soup.find("table",{"class":"tb01"}).find_all('tr' )

# print(all_url)


for i in all_url:
    view=re.findall(r'.*?">(.*?)</td>', str(i))
    with open('c:\ks.txt','a') as f:
        f.write(str(view)+'\n')
    print(view)

# kj=all_url.find_all("tr",{"style":"height: 23.25pt;"})
# print(all_url)
# for each in all_url:
#     print(each)
#     print(each.img['alt'])
#     for tt in each:
#         aa=tt.find('a')
#         print(aa.text)
#         for aa in tt:
#              print(aa)

#     print(all_url)

