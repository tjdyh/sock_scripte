#!/usr/bin/env python
#encoding:utf-8
'''
__Author__:lll
'''

def test_func1(*args):
    for index, one_char in enumerate(args):
        print('index={0}, one_char={1}'.format(index, one_char))

def test_func2(*args):
    print(type(args))
    print(args)
    print(",".join(args))
    print(str(args))
    print(list(args))
    for i in range(len(list(args))):
        print(list(args)[i])

if __name__ == '__main__':
    print("脚本之家测试结果：")
#    str_list=['白','利','光']
    str_list1=["10.0.254.158","10.0.254.159"]
#    test_func1(*str_list)
    test_func2(*str_list1)
