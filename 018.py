from bs4 import BeautifulSoup
import requests
import gevent
from gevent import monkey,pool
monkey.patch_all()
jobs=[]
links=[]
p=pool.Pool(10)
urls = [
    'https://www.taobao.com/',
    # 'http://www.tendyron.com',
]
def get_links(url):
    r = requests.get(url)
    print(r.text)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,'lxml')
        links + soup.find_all('a')
for url in urls:
    jobs.append(p.spawn(get_links, url))
gevent.joinall(jobs)