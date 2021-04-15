""" 你用 lambda 定义了一个匿名函数，并想在定义时捕获到某些变量的值。"""

if __name__ == "__main__":
    x = 10
    a = lambda y: x + y
    x = 20
    b = lambda y: x + y
    print(a(10))
    print(b(10))

    # lambda 表达式中的 x 是一个自由变量，在运行时绑定值，而不是定义时就绑定
    # 因此在调用这个 lambda 表达式的时候，x 的值是执行时的值

    # 如果你想让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可
    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y
    print(a(10))
    print(b(10))

    # FAQ
    funcs = [lambda x: x+n for n in range(5)]
    for f in funcs:
        print(f(0))

    # right way 
    funcs = [lambda x, n=n: x+n for n in range(5)]
    for f in funcs:
        print(f(0))