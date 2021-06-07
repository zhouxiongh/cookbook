""" 你想要扩展函数中的某个闭包，允许它能访问和修改函数的内部变量。 """

def sample():
    n = 0
    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

if __name__ == "__main__":
    # 通常来讲，闭包的内部变量对于外界来讲是完全隐藏的。但是，你可以通过编写访
    # 问函数并将其作为函数属性绑定到闭包上来实现这个目的
    f = sample()
    f()
    f.set_n(10)
    f()
    print(f.get_n())

    # nonlocal 声明可以让我们编写函数来修改内部变量的值
    # 函数属性允许我们用一种很简单的方式将访问方法绑定到闭包函数上