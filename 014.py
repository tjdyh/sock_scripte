#!/usr/bin/env python

import paramiko

transport = paramiko.Transport(('10.0.254.158',22))
transport.connect(username='root', password='Eaj2018!@#$%^')
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('/tmp/444.jpg','/tmp/333.jpg')
sftp.get('/tmp/abc.txt',r'/tmp/abc.txt')
transport.close()