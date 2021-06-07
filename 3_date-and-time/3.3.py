"""
你需要将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节
"""

if __name__ == "__main__":
    x = 1234.56789
    print(format(x, '0.2f'))
    print(format(x, '>10.1f'))
    print(format(x, '<10.1f'))
    print(format(x, '^10.1f'))
    print(format(x, ','))
    print(format(x, '0.2E'))
    print(format(x, 'e'))