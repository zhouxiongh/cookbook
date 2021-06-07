""" 你想构造一个可接受任意数量参数的函数 """

# 为了能让一个函数接受任意数量的位置参数，可以使用一个 * 参数
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

# 一个 * 参数只能出现在函数定义中最后一个位置参数后面，而**参数只能出现在最后一个参数
def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass

if __name__ == '__main__':
    print(avg(1, 2, 3, 4))