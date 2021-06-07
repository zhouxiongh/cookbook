""" 
你的代码中需要依赖到回调函数的使用 (比如事件处理器、等待后台任务完成后的
回调等)，并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到 
"""

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

def make_handler1():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

if __name__ == "__main__":
    # apply_async(add, (2, 3), callback = print_result)
    # apply_async(add, ('hello', 'world'), callback = print_result)

    # 为了让回调函数访问外部信息，一种方法是使用一个绑定方法来代替一个简单函数
    # r = ResultHandler()
    # apply_async(add, (2, 3), callback = r.handler)
    # apply_async(add, ('hello', ' world'), callback = r.handler)

    # 第二种方式，作为类的替代，可以使用一个闭包捕获状态值
    # handler = make_handler()
    # apply_async(add, (2, 3), callback = handler)
    # apply_async(add, ('hello', ' world'), callback = handler)
    # 还有另外一个更高级的方法，可以使用协程来完成同样的事情
    handler = make_handler1()
    # Advance to the yield
    next(handler)
    apply_async(add, (2, 3), callback = handler.send)
    apply_async(add, ('hello', ' world'), callback = handler.send)

    # 可以在一个对象实例 (通过一个绑定方法) 或者在一个闭包中保存它
    # 两种方式相比，闭包或许是更加轻量级和自然一点，因为它们可以很简单的通过函数来构造


