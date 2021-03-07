#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/2

""" 
使用多个界定符分割字符串
"""
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
re.split(r'[;,\s]\s*', line)
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

