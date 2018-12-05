import requests
import time
from lxml import etree
url = ("https://alpha.wallhaven.cc/search?q=girl&categories=111&purity=100&sorting=relevance&order=desc")
html = requests.get(url)
selector = etree.HTML(html.text)
#print(html.text)
print(selector)
for i in range(10):
    print(i)