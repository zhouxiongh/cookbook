#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/7_fun

""" 
将 Unicode 文本标准化
"""
import unicodedata

if __name__ == '__main__':
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    print(s1)
    print(s2)
    print(s1 == s2)
    print("s1 len:", len(s1))
    print("s2 len:", len(s2))
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print(t1, t2)
    print(t1 == t2)


