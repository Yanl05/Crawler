import requests

if __name__ == '__main__':
    target = 'http://www.biqukan.com/0_790/15948251.html'
    req = requests.get(url=target)
    print(req.text)