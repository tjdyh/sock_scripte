# coding: utf-8
__author__ = 'blg'

import threading, time

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global  n, lock
        time.sleep(1)
        if lock.acquire():
            print(n, self.name)
            n += 1
            lock.release()

if __name__ == '__main__':
    n = 1
    threadlist = []
    lock = threading.Lock()
    for i in range(1, 200):
        t = MyThread()
        threadlist.append(t)
    print(threadlist)
    for t in threadlist:
        t.start()
    for t in threadlist:
        t.join()