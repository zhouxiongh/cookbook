#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/7

"""
在正则式中使用 Unicode
"""
import re

if __name__ == '__main__':
    num = re.compile(r'\d+')
    if num.match('123'):
        print('math ascii number')
    if num.match('\u0661\u0662\u0663'):
        print('math Arabic digits')
    # print('hello world')

