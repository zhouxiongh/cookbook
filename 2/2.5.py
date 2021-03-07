#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/5

""" 
字符串搜索和替换
"""
import re
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


if __name__ == '__main__':
    # 对于简单的字面模式，直接使用 str.repalce() 方法即可
    text = 'yeah, but no, but yeah, but no, but yeah'
    text = text.replace('yeah', 'yep')
    print(text)
    # 对于复杂的模式，请使用 re 模块中的 sub() 函数
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    # text = datepat.sub(r'\3-\1-\2', text)
    print(text)
    # 对于更加复杂的替换，可以传递一个替换回调函数来代替
    text, n = datepat.subn(change_date, text)
    print('replace text:{} | replace times:{}'.format(text, n))





