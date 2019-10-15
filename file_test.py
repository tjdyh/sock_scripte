# -*-coding:utf-8-*-

import os,sys
from pprint import pprint
import logging

def log(msg):
    # 创建logger，如果参数为空则返回root logger
    logger = logging.getLogger("blg")
    # 设置logger日志等级
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        fh = logging.FileHandler("test.log", encoding="utf-8")
        ch = logging.StreamHandler()
        formatter = logging.Formatter(
                        fmt="%(asctime)s %(name)s %(levelname)s %(message)s",
                        datefmt='%Y-%m-%d  %H:%M:%S %a')
        # 为handler指定输出格式，注意大小写
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 为logger添加的日志处理器
        logger.addHandler(fh)
        logger.addHandler(ch)
    logger.debug(msg)

log(sys.path)
# pprint(sys.path)
current_dir = os.getcwd()
# pprint(current_dir)
log(current_dir)
# 定义一个工作目录
def defWokSpace(work_dir):
    if os.path.exists(work_dir):
        # pprint('目录已存在，目录名为：%s' %workdir)
        log('目录已存在，目录名为：%s' %workdir)
    else:
        workspace = os.mkdir(work_dir)
        log('已生成工作目录：%s' %work_dir)
def appendInfo(file_name,info_msg):
    if os.path.exists(file_name):
        log('文件存在！文件名为：%s' %file_name)
        with open(file_name, 'a') as f:
            f.writelines(info_msg)
    else:
        log('文件不存在')
        with open(file_name, 'w') as f:
            f.writelines(info_msg)

if __name__ == '__main__':
    file_name = 'info.txt'
    info_msg = '127.0.0.2 root 22 /home/tomcat/webapps/\n'
    workdir = 'workspace'
    defWokSpace(workdir)
    appendInfo(file_name,info_msg)

