from itertools import groupby
from operator import itemgetter

rows = [{'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
        ]

if __name__ == '__main__':
    rows.sort(key=itemgetter('date'))
    # groupby() 函数扫描整个序列并且查找连续相同值 (或者根据指定 key 函数返回值
    # 相同) 的元素序列。
    for date, items in groupby(rows, key=itemgetter('date')):
        # 在每次迭代的时候，它会返回一个值和一个迭代器对象，这个迭代
        # 器对象可以生成元素值全部等于上面那个值的组中所有对象
        print(date)
        for i in items:
            print(' ', i)
