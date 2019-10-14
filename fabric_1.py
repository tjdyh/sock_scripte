#!/usr/bin/env python
import getpass
from fabric import task
from fabric import config
from fabric import Connection,Config
from fabric import group
from fabric import transfer
from pprint import pprint
from fabric import SerialGroup

# host = '192.168.88.12'
# user = 'root'
# port = 22
##################################################################################################
# password = getpass.getpass("What's your password?\n")
# config = Config(overrides={'password':password})
#
# conn = Connection(host=host,user=user,port=port,connect_kwargs={'password':password})
# # conn = Connection(host=host,user=user,port=port,config=config)
# conn.run('uname -a')
#
# tran = transfer.Transfer(conn)
# # tran.put("aaa.txt","/tmp")
# tran.get('/tmp/aaa.txt','/tmp/abc.txt')
###################################################################################################

class Appdeploy(Connection,transfer.Transfer):
    def __init__(self, host, port, username, password):
        self.host = host;
        self.port = port;
        self.username = username;
        self.password = password;

    # def app_connect(self):
    #     conn = Connection(host=self.host,port=self.port,user=self.username,connect_kwargs={'password':self.password})
    #     return conn

    def app_transfer(self,):
        conn = Connection(host=self.host, port=self.port, user=self.username, connect_kwargs={'password': self.password})
        tran = Transfer(conn)
        return tran


if __name__ == '__main__':
    host = '192.168.88.12'
    port = 22
    username = 'root'
    password = '123456'
    ob_pro = Appdeploy(host,port,username,password)
    pprint(type(ob_pro))

