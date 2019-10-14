#!/usr/bin/env python

import sys
import pyperclip

PASSWORDS = {'blg':'123456','blog':'888888','lulu':'123456'}

if len(sys.argv)<2:
    print('Usage: py 010.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)