from collections import OrderedDict
import json
from operator import itemgetter

rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]


def order_dict():
    d = OrderedDict()
    d['foo'] = 4
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 1

    # 在迭代操作的时候它会保持元素被插入时的顺序
    # for key in d:
    #     print(key, d[key])

    return d


def sort_by_key(rows, key):
    return sorted(rows, key=itemgetter(key))


if __name__ == '__main__':
    print(json.dumps(order_dict()))
    print(sort_by_key(rows, 'fname'))
    print(sort_by_key(rows, 'uid'))
