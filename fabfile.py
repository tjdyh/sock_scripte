#!/usr/bin/env python
from fabric import task
from fabric import Connection
from fabric import group
from fabric import transfer
from pprint import pprint

#hosts=["'10.0.254.158'","'10.0.254.159'","'10.0.254.160'"]

#group = group.SerialGroup(hosts, user='root',connect_kwargs={'password':'Eaj2018!@#$%^'})
passwd = "Eaj20191qaz"
conn = Connection(host='10.0.254.158', user='root', connect_kwargs={'password':passwd})





@task
def uname_local(c):
    c.run('uname -a')


@task
def ls_remote(c,dir_path):
    with conn.cd(dir_path):
        conn.run("ls -la")


@task
def uname_rmt(c,host,user,password):
    con = Connection(host, user=user, connect_kwargs={'password':password})
    con.run("uname -a")


@task
def uname_test(c):
    group1 = group.SerialGroup('10.0.254.158','10.0.254.159','10.0.254.160', user='root', connect_kwargs={'password':passwd})
    group1.run("uname -a")

@task
def uname_test1(c,host):
    con = Connection(host, user='root', connect_kwargs={'password':passwd})
    con.run("uname -a")

@task
def upload_rmt(c,host):
    con = Connection(host, user='root', connect_kwargs={'password':passwd})
    tran = transfer.Transfer(con)
    pprint("上传文件。。。")
    tran.put('/tmp/abc.txt', '/tmp')
    pprint("上传完成！")



@task
def uploadApp(c,host,port):
    con = Connection(host, user='root', port=port, connect_kwargs={'password':passwd})
    tran = transfer.Transfer(con)
    pprint("开始上传程度包。。。")
    tran.put('/var/lib/jenkins/workspace/600_eboss_omsweb/`date "+%Y%m%d"`/*.war','/tmp/')
    pprint("上传完成！")