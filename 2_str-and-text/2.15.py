"""
你想创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。
"""

if __name__ == "__main__":
    s = '{name} has {n} messages.'
    # print(s.format(name='guido', n=37))
    name = 'guido'
    n = 37
    print(s.format_map(vars()))