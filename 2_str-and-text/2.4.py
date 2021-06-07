#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/3

""" 
字符串匹配和搜索
"""
import re

if __name__ == '__main__':
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text == 'yeah')
    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'
    # datepat = re.compile(r'\d+/\d+/\d+')
    # 在定义正则式的时候，通常会利用括号去捕获分组
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    if datepat.match(text1):
        print('yes')
    else:
        print('no')
    if datepat.match(text2):
        print('yes')
    else:
        print('no')

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print(datepat.findall(text))
