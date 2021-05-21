"""
在子类中，你想要扩展定义在父类中的 property 的功能。
"""

class Person:
    def __init__(self, name) -> None:
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('expected a str')
        self._name = value

    @name.deleter
    def name(self):
        raise ArithmeticError("can't delete attribute")

class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name
    
    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


if __name__ == "__main__":
    s = SubPerson('Guido')
    print(s.name)
    s.name = 'Larry'
    # s.name = 42