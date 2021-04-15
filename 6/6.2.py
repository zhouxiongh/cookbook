"""
你想读写 JSON(JavaScript Object Notation) 编码格式的数据
"""

import json
from pprint import pprint

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23,
    'data' : {
        'name' : 'ACME',
        'shares' : 100,
        'price' : 542.23,
    },
}

list_data = ['spam', 'spam', 'eggs', 'spam']



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


classes = {
    'Point' : Point
}

def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

if __name__ == "__main__":
    # 其中两个主要的函数是 json.dumps() 和 json.loads()
    pprint(list_data)
    json_str = json.dumps(list_data)
    print(json_str, type(json_str))
    list_data = json.loads(json_str)
    print(list_data, type(list_data))
    # 为了遵循 JSON 规范，你应该只编码 Python 的 lists 和 dictionaries

    # 对象实例通常并不是 JSON 可序列化的
    p = Point(3, 4)
    s = json.dumps(p, default=serialize_instance)
    a = json.loads(s, object_hook=unserialize_object)
    print(s)
    print(a)
    print(a.x)
    print(a.y)

    
