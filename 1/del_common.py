def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe1(items, key=None):
    seen = set()
    for item in items:
        val = items if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe(a)))
    # print(list(dedupe(b)))  unhashable type: 'dict'
    # 基于 x and y 消除重复元素
    print(list(dedupe1(b, key=lambda d: (d['x'], d['y']))))
    # 基于 x or y 消除重复元素
    print(list(dedupe1(b, key=lambda d: d['x'])))
    print(list(dedupe1(b, key=lambda d: d['y'])))
