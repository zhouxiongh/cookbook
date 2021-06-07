a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {'w': 10, 'x': 11, 'y': 2}

if __name__ == '__main__':
    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(a.items() & b.items())
    c = {key: a[key] for key in a.keys() - {'z', 'x'}}
    print(c)