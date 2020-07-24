"""
Question: 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
"""

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    my_list = [1, 4, -5, 10, -7, 2, 3, -1]
    pos = [n for n in my_list if n > 0]
    neg = [n for n in my_list if n < 0]
    print('(pos:{}, neg:{})'.format(pos, neg))
    # 列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果
    # 集，占用大量内存
    ivals = list(filter(is_int, values))
    print(ivals)
