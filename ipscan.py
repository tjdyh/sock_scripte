# -*- coding: utf-8 -*-

import socket, time, threading
socket.setdefaulttimeout(3)

def socket_port(ip, port):
    """
    输入IP和端口号，扫描判断端口是否占用
    :param ip:
    :param port:
    :return:
    """
    try:
        if port >= 65535:
            print(u'端口扫描结束')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(ip,u':',port,u'端口已占用')
    except:
        # print("端口扫描异常")
        pass

def ip_scan(ip):
    """
    输入IP，扫描IP的0~65534端口情况
    :param ip:
    :return:
    """
    try:
        print(u'开始扫描 %s' % ip)
        star_time=time.time()
        thread_list = []
        for i in range(0, 65534):
            t = threading.Thread(target=socket_port, args=(ip, int(i)))
            t.start()
            thread_list.append(t)
        for t in thread_list:
            t.join()
        print(u'妈蛋！累死了，扫描端口完成，总共用时：%.2f' % (time.time()-star_time))
    except:
        print(u'扫描IP出错')

if __name__ == '__main__':
    url = input('Input the ip you want to scan:')
    ip_addr = socket.gethostbyname(url)
    print(ip_addr)
    ip_scan(ip_addr)