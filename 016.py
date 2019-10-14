#!coding:utf-8
import threading
import urllib.request
def get_body(i):
    print("start",i)
    urllib.request.urlopen("http://www.baidu.com")
    print("end",i)

for i in range(3):
    t = threading.Thread(target=get_body,args=(i,))
    t.start()