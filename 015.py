#! coding:utf-8
import gevent
from gevent import monkey;monkey.patch_all()
import urllib.request
def get_body(i):
    print("start",i)
    urllib.request.urlopen("http://www.baidu.com")
    print("end",i)

tasks=[gevent.spawn(get_body,i) for i in range(3)]
gevent.joinall(tasks)