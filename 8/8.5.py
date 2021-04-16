""" 你想封装类的实例上面的“私有”数据，但是 Python 语言并没有访问控制。"""

class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass

class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        pass


if __name__ == '__main__':
    # 使用双下划线开始会导致访问名称变成其他形式。比如，在前面的类 B 中，私有
    # 属性会被分别重命名为_B__private 和 _B__private method 
    # 这样重命名的目的是什么，答案就是继承——这种属性通过继承是无法被覆盖的
    
    # 大多数而言，你应该让你的非公共名称以单下划线开头
    # 如果你清楚你的代码会涉及到子类，并且有些内部属性应该在子类中隐藏
    # 起来，那么才考虑使用双下划线方案 