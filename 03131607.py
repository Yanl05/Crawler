#   爬壁纸
import os
import requests
import time
import random
from lxml import etree

keyWord = input(f"{'Please input the keywords that you want to download:'}")  # f 格式化控制依旧遵循 format 规范

class Spider():
    # 1.初始化参数
    def __init__(self):
        #   headers 是请求头
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
        #   filepath是文件储存路径，与文件的根目录相同
        self.filePath = ('/pathon test/爬壁纸/' + keyWord + '/')

    #   2.创建本地文件路径，储存图片
    def creat_Flie(self):
        filePath = self.filePath    #   调用初始化函数的方法
        if not os.path.exists(filePath):
            os.makedirs(filePath)   #   如果路径不存在，则通过os创建 makedirs()

    #   3.从网页获取总图片数，用以一直循环爬取
    def get_pageNum(self):
        total = ''
        #   通过输入的关键字找到对应的url
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc").format(keyWord)
        html = requests.get(url)
        selector = etree.HTML(html.text)
        pageInfo = selector.xpath('//header[@class="listing-header"]/h1/text()')
        #   把信息放入pageInfo 成为一个元组
        string = str(pageInfo[0])   #   选取pageinfo里第一个元组的内容
        numlist = list(filter(str.isdigit, string))  #  filter判断string中是否是数字，是的话放入list重新组合为一个列表
        for item in numlist:
            total += item   #   把新列表numlist的每个元素变成一个字符串
        totalPagenum = int(total)
        return totalPagenum


    #   4.找到图片链接
    def getLinks(self, number): #   number是页面数
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc&page={}").format(keyWord, number)
        try:
            html = requests.get(url)
            selector = etree.HTML(html.text)
            pic_Linklist = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
        except Exception as e:
            print(repr(e))
        return pic_Linklist


    #   5.得到图片链接然后下载图片
    def download(self, url, count):
        string = url.strip('/thumbTags').strip('https://alpha.wallhaven.cc/wallpaper/') #   strip('**')去除头尾的**字符
        html = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + string + '.jpg'
        pic_path = (self.filePath + keyWord + str(count) + '.jpg')
        try:
            start = time.time()
            pic = requests.get(html, headers = self.headers)
            f = open(pic_path, 'wb')    #   以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
            f.write(pic.content)    #   如果想取文本，可以通过r.text。如果想取图片，文件，则可以通过r.content
            f.close()
            end = time.time()
            print(f"Image :{count} has been download, cost : ", end - start, 's')
        except Exception as e:
            print(repr(e))


    #   6.主函数，爬取图片后计数，显示交互信息
    def main_fuction(self):
        #   count 是图片数量 times是总页面数
        self.creat_Flie()
        count = self.get_pageNum()
        print("We found :{} images!".format(count))
        times = int(count/24 + 1)
        j = 1
        start = time.time()
        for i in range(times):
            pic_Urls = self.getLinks(i + 1)
            start2 = time.time()
            for item in pic_Urls:
                self.download(item, j)
                j += 1
            end2 = time.time()
            print("This page cost: ", end2 - start2, 's')
        end = time.time()
        print("Total page cost: ", end - start, 's')


spider = Spider()   #  实例化类
spider.main_fuction()   #运行主函数