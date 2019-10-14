#!/usr/bin/env python
#coding:utf-8

import re
mo_str = input("请输入要茶杯的字符串：")
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search(mo_str)
print(mo.group())