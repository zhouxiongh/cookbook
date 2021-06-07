#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/5

""" 
最短匹配模式
"""
import re

if __name__ == '__main__':
    # str_pat = re.compile(r'\"(.*)\"')
    # 可以在模式中的 * 操作符后面加上? 修饰符,这样就使得匹配变成非贪婪模式，从而得到最短的匹配
    str_pat = re.compile(r'\"(.*?)\"')
    text1 = 'Computer says "no."'
    print(str_pat.findall(text1))
    text2 = 'Computer says "no." Phone says "yes."'
    print(str_pat.findall(text2))

