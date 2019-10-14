# -*-coding:utf-8-*-

import os
from pprint import pprint

current_dir = os.getcwd()
pprint(current_dir)
# 定义一个工作目录
workspace = os.mkdir()
def appendDir(file_name,info_msg):
    if os.path.exists(file_name):
        pprint('文件存在！')
        with open(file_name, 'a') as f:
            f.writelines(info_msg)
    else:
        pprint('文件不存在')
        with open(file_name, 'w') as f:
            f.writelines(info_msg)

if __name__ == '__main__':
    file_name = 'info.txt'
    info_msg = '127.0.0.1 root 22 /home/tomcat/webapps/\n'
    appendDir(file_name,info_msg)

