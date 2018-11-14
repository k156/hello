class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s


class Paral:
    x, y = 0, 0

    def __init__(self, name):
        self.name = name

    def input_data(self, msg):
        user_input = input(msg)
        data = user_input.split(',')
        x, y = Casting.to_int(data[0], data[1])

    def multiply(self, x , y):
        A = x * y
        print(self.name"의 면적은 {}입니다.".format(A))


class Rect(Paral):
    name = "직사각형"

class Square(Rect):
    name = "정사각형"
    
    def multiply(self, x):
        A = x * x
        print(self.name"의 면적은 {}입니다.".format(A))


whichquad = input("사각형의 종류는? \n 1)평행사변형 \n 2)직사각형 \n 3)정사각형 \n")


all_quads = []
if whichquad == 1:
    paral = Paral()
    paral.input_data()
    paral.multiply()  



if whichquad == 2:
    exit()

if whichquad == 3:
    exit()
