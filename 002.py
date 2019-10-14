#!/usr/bin/env python
#coding:utf-8




def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

if __name__ == '__main__':
    x=input('请输入你的内容：')
    print(type(x))
    x=eval(x)
    a = my_abs(x)
    print(a)
