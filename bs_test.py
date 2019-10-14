#!/usr/bin/env python3
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
from urllib import request
from urllib import error
from pprint import pprint

def getHtml(url):
    try:
        html = request.urlopen(url)
    except error.HTTPError as e:
        return None
    soup = BeautifulSoup(html, "lxml")
    # pprint(soup.prettify())
    # pprint(soup)
    for link in soup.find_all('a'):
        pprint(link.get('href'))

if __name__ == '__main__':
    url = "http://www.baidu.com"
    getHtml(url)