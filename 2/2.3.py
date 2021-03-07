#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/3

""" 
用 Shell 通配符匹配字符串
"""
from fnmatch import fnmatch, fnmatchcase

if __name__ == '__main__':
    print(fnmatch('foo.txt', '*.txt'))
    print(fnmatchcase('foo.txt', '*.TXT'))
