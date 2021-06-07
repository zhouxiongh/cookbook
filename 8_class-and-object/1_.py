""" 你想改变对象实例的打印或显示输出，让它们更具可读性。 """

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

if __name__ == "__main__":
    p = Pair(3, 4)
    print(p)

    # 自定义 repr () 和str () 通常是很好的习惯，因为它能简化调试和实例输出
