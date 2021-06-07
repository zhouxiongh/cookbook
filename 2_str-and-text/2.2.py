#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/2_str-and-text

""" 
字符串开头或结尾匹配
"""

filename = 'spam.txt'
filename.endswith('txt')
filename.startswith('file:')

url = 'http://www.python.org'
url.startswith('http:')

# 检查多种匹配
filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
var = [name for name in filenames if name.endswith(('.c', '.h'))]
print(var)

