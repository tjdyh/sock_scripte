#!/usr/bin/env python
from fabric import task
from fabric import Connection

con = Connection(host='10.0.254.158', user='root', connect_kwargs={'password':'Eaj2018!@#$%^'})

@task
def remote_task(con):
    con.run('uname -a')

