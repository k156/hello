class TestClass:
    name = "TEST"

    def __init__(self):
        print("TTTTTTT")

    def static_method():
        print("STATIC!!")
    
    def get_name(self):
        print('QQQQQQQQQ')
        return self.name

    def area(self, x, y):
        return x * y


class Child(TestClass):
    def __init__(self):
        super().__init__()
        print("My init!!!")

    def get_name(self):
        t = super().get_name()
        return "Child Name" + self.name

    def area(self, x, y):
        t = super().area(x, y)
        return t/2


test =TestClass()
child =Child()

getattr(test, 'get_name')()
getattr(TestClass, 'static_method')()

