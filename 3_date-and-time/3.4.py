"""
你需要转换或者输出使用二进制，八进制或十六进制表示的整数。
"""

if __name__ == "__main__":
    x = 1234
    print(bin(x))
    print(oct(x))
    print(hex(x))

    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))

    # Python 指定八进制数的语法跟其他语言稍有不同
    # 需确保八进制数的前缀是 0o 