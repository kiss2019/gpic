import os
import re
import requests
from bs4 import BeautifulSoup
url="http://www.pinble.com/Lottery.htm"
url2="http://www.pinble.com/LotteryOneList.aspx?type=88FBC9101C364354&class=%E5%85%A8%E5%9B%BD%E7%A6%8F%E5%BD%A9&name=%E4%B8%83%E4%B9%90%E5%BD%A9"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Accept-Encoding': 'gzip',
    "Content-Type":"application/x-www-form-urlencoded",
    "Referer":"http://www.pinble.com/Lottery.htm"
}   #头部文件
data={
    '__VIEWSTATE':'	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',
    '__VIEWSTATEGENERATOR':	'8FD8C755',
    '__EVENTTARGET':	'AspNetPager1',
    '__EVENTARGUMENT':	'1',
    'AspNetPager1_input':	'0'
}
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
def getliveid(url,data):

    global 变化参数
    try:
        r = requests.post(url2, headers=headers, data=data,timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        data = r.content.decode('utf-8')
        soup=BeautifulSoup(data,'lxml')
        res =soup.find_all('tr',style="background-color:White;border-color:#B6CBE8;")

        for i in res:
            bb=i.find_all('td')
            开奖时间=bb[0].get_text().strip()
            期号=bb[1].get_text().strip()
            开奖号码=bb[2].get_text().strip()
            print(开奖时间,期号,开奖号码)
        soup = BeautifulSoup(data, 'lxml')
        res2 = soup.find_all('font',color="blue")
        page=re.findall(r'\d\d+',str(res2[1]))
        print('页数共计{}页'.format(page))

        soup=BeautifulSoup(data,'lxml')
        变化参数 =soup.find('input')['value']
        # print(变化参数)
        return 变化参数
    except:
        return "产生异常"

def getuserid(liveid):
    live_url="https://www.huajiao.com/l/{}".format(liveid)
    print(live_url)
    res=requests.get(live_url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')

    text=soup.title.get_text()
    # print(text)
    userid=re.findall(r'ID:([1-9]\d\d+)',text)
    print(userid[0])
    return userid

def getuserdata(userid):
    print("正在获取id为:{}的主播信息".format(userid))
    result=requests.get('https://www.huajiao.com/user/{}'.format(userid),headers=headers)
    soup=BeautifulSoup(result.text,'html.parser')
    userinfo=soup.find('div',{'id':'userInfo'})
    # print(type(userinfo))
    data={}
    data['actor']=userinfo.find('div',{'class':'avatar'}).img.attrs['src'] #小图
    data['actor']=data['actor'][:-12]+data['actor'][-4:] #转成大图
    # print(data['actor'])
    # print(userinfo)
    data['userid']=userid
    tmp=userinfo.h3.get_text('|',strip=True).split('|')#用|分开
    data['Username']=tmp[0]
    data['area']=tmp[2]
    tmp=userinfo.find('ul',{'class':'clearfix'}).get_text('|',strip=True).split('|')
    data['follow']=tmp[0]
    data['followed']=tmp[2]
    data['supported']=tmp[4]
    data['experience']=tmp[6]
    print(data)
    return data

# r = requests.post(url2, headers=headers, data=data, timeout=20)
# r.raise_for_status()
#
# r.encoding = r.apparent_encoding
# data = r.content.decode('utf-8')
变化参数=getliveid(url2,data)

for i in range(50):
    data['__VIEWSTATE'] = 变化参数
    data['__EVENTARGUMENT']=i+1
    data['AspNetPager1_input']=i
    # print(data)
    变化参数=getliveid(url2,data)



