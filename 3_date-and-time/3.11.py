"""
你想从一个序列中随机抽取若干元素，或者想生成几个随机数。
"""

if __name__ == "__main__":
    import random
    values = [1,2,3,4,5]
    print(random.choice(values))
    print(random.sample(values, 2))
    print(random.randint(0, 10))
    print(random.random())