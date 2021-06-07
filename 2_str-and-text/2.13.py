"""
问题：你想通过某种对齐方式来格式化字符串
"""

if __name__ == "__main__":
    text = 'Hello World'
    print(text.ljust(20))
    print(text.rjust(20, '='))
    print(text.center(20, '*'))
    print(format(text, '>20'))
    print(format(text, '<20'))
    print(format(text, '^20'))
