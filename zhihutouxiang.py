import requests
import urllib
import re
import random
from time import sleep
def main():
    url= 'https://www.zhihu.com/'
    #感觉这个话题下面美女多
    #headers={' '}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Host': 'www.zhihu.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,en-US;q=0.8,en;q=0.6',
        'Origin': 'https://www.zhihu.com/',
        'Connection': 'keep-alive',
        'Referer': 'https://www.zhihu.com/question/22591304/followers',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Xsrftoken': '你自己的_xsrf',
        'Cookie': '巴拉巴拉一大长串'
    }

    i=1
    for x in range(20,3600,20):
        data={'start':'0',
        'offset':str(x),
        '_xsrf':'a128464ef225a69348cef94c38f4e428'}
        #知乎用offset控制加载的个数，每次响应加载20
        content=requests.post(url,headers=headers,data=data,timeout=10).text
        #用post提交form data
        imgs=re.findall('<img src=\\\\\"(.*?)_m.jpg',content)
        #在爬下来的json上用正则提取图片地址，去掉_m为大图
        for img in imgs:
            try:
                img=img.replace('\\','')
                #去掉\字符这个干扰成分
                pic=img+'.jpg'
                path='d:\\bs4\\zhihu\\jpg\\'+str(i)+'.jpg'
                #声明存储地址及图片名称
                urllib.urlretrieve(pic,path)
                #下载图片
                print(u'下载了第'+str(i)+u'张图片')
                i+=1
                sleep(random.uniform(0.5,1))
                #睡眠函数用于防止爬取过快被封IP
            except:
                print(u'抓漏1张')
                pass
        sleep(random.uniform(0.5,1))

if __name__=='__main__':
    main()

