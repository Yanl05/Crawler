import requests
import time
from lxml import etree
url = ("https://alpha.wallhaven.cc/search?q=girl&categories=111&purity=100&sorting=relevance&order=desc")
html = requests.get(url)
selector = etree.HTML(html.text)
#print(html.text)
#print(selector)

#pageInfo = selector.xpath(f'//header[@class="listing-header"]/h1/text()')
total = ''
pageInfo = selector.xpath('//header[@class="listing-header"]/h1[1]/text()')
string = str(pageInfo[0])
numlist = list(filter(str.isdigit, string))  #  filter判断string中是否是数字，是的话放入list重新组合为一个列表
for item in numlist:
    total += item
print(total)


a = 'a'
b = 'b'
c = ''
c = a + b
print(c)

url = ("https://alpha.wallhaven.cc/search?q=girl&categories=111&purity=100&sorting=relevance&order=desc&page=3")
html = requests.get(url)
selector = etree.HTML(html.text)
pic_Linklist = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
#print(pic_Linklist)
#print(repr(e))
d = time.time()
print(d)
print("time.time(): %f " % time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))