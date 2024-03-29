#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(1)
        # time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        time.sleep(2)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()