#   爬壁纸  多线程
import os
import requests
import time
from lxml import etree
from threading import Thread

keyWord = input(f"{'Please input the keyword that you want to download:'}")
class Spider():
    #   初始化参数
    def __init__(self):
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        }
        #   代理IP，当访问网站受限制时，需要切换IP
        self.proxies = {"http": "http://61.178.238.122:63000"}
        self.filePath = ('/pathon test/爬壁纸/' + keyWord + '/')

    #   2.创建本地文件路径，储存图片
    def craet_File(self):
        filePath = self.filePath
        if not os.path.exists(filePath):
            os.makedirs(filePath)

    #   3.从网页获取总图片数，用以一直循环爬取
    def get_pageNum(self):
        total = ""
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc").format(keyWord)
        html = requests.get(url, headers = self.headers, proxies = self.proxies)
        selector = etree.HTML(html.text)
        pageInfo = selector.xpath('//header[@class="listing-header"]/h1/text()')
        string = str(pageInfo[0])
        numlist = list(filter(str.isdigit, string))
        for item in numlist:
            total += item
        totalPagenum = int(total)
        return totalPagenum


    #   4.找到图片链接
    def getLinks(self, number):
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc&page={}").format(keyWord, number)
        try:
            html = requests.get(url, headers = self.headers, proxies = self.proxies)
            selector = etree.HTML(html.text)
            pic_Linklist = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
        except Exception as e:
            print(repr(e))
        return pic_Linklist

    #   5.得到图片链接然后下载图片
    def download(self, url, count):
        string = url.strip('/thumbTags').strip('https://alpha.wallhaven.cc/wallpaper/')     # strip('**')去除头尾的**字符
        html = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + string + '.jpg'
        pic_path = (self.filePath + keyWord + str(count) + '.jpg')
        try:
            start = time.time()
            pic = requests.get(html, headers = self.headers)
            f = open(pic_path, 'wb')
            f.write(pic.content)
            f.close()
            end = time.time()
            print(f"Image {count} has been download, cost: ", end - start, 's')
        except Exception as e:
            print(repr(e))


    #   6.主函数，爬取图片后计数，显示交互信息
    def main_fuction(self):
        # count是图片总数 times是总页面数
        self.craet_File()
        count = self.get_pageNum()
        print("We found :{} image! ".format(count))
        times = int(count/24 + 1)
        j = 1
        start = time.time()
        for i in range(times):
            pic_Urls = self.getLinks(i + 1)
            start2 = time.time()
            threads = []
            for item in pic_Urls:
                t = Thread(target = self.download, args = [item, j])
                t.start()
                threads.append(t)
                j += 1
            for t in threads:
                t.join()
            end2 = time.time()
            print("This page cost: ", end2 - start2, 's')
        end = time.time()
        print("Total cost : ", end - start, 's')

spider = Spider()
spider.main_fuction()