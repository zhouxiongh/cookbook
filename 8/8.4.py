""" 你的程序要创建大量 (可能上百万) 的对象，导致占用很大的内存
对于主要是用来当成简单的数据结构的类而言，你可以通过给类添加
slots属性来极大的减少实例所占的内存
"""

class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class Date1:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


if __name__ == "__main__":
    # 当你定义slots后，Python 就会为实例使用一种更加紧凑的内部表示
    # 为了给你一个直观认识，假设你不
    # 使用 slots 直接存储一个 Date 实例，在 64 位的 Python 上面要占用 428 字节，而如果
    # 使用了 slots，内存占用下降到 156 字节 

    # import sys
    # d = Date(2012, 12, 21)
    # d1 = Date1(2012, 12, 21)
    # print(sys.getsizeof(d))
    # print(sys.getsizeof(d1))