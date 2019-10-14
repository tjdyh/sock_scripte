from bs4 import BeautifulSoup
import urllib.request
import gevent
from gevent import monkey,pool
monkey.patch_all()
jobs=[]
links=[]
p = pool.Pool(10)
urls = [
    'https://www.taobao.com/',
]
def get_links(url):
    r = urllib.request.urlopen(url)
    # print(r.getcode())
    # print(r.read().decode('utf-8'))
    if r.getcode()== 200:
        # print('OK')
        soup = BeautifulSoup(r.read().decode('utf-8'),'lxml')
        for hr in soup.find_all('a'):
            if str(hr.get('href'))[:4]=='http':
                links.append(hr.get('href'))
        # print(soup.find_all('a'))
        print(links)

for url in urls:
    jobs.append(p.spawn(get_links, url))

gevent.joinall(jobs)