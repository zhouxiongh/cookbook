"""
你想将几个小的字符串合并为一个大的字符串
"""

if __name__ == "__main__":
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print(" ".join(parts))

    # 特别的，你永远都不应像下面这样写字符串连接代码
    # s = ''
    # for p in parts:
    #   s += p
    data = ['ACME', 50, 91.1]
    print(','.join(str(d) for d in data))

    # 避免不必要的连接操作
    a,b,c = '1','2','3'
    print(a + ':' + b + ':' + c) # Ugly
    print(':'.join([a, b, c])) # Still ugly
    print(a, b, c, sep=':') # Better