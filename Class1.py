class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s


class Paral:
    def __init__(self, name):
        self.name = name

    def Calc(self):
        user_input = input(" ex) 3,4 ")
        data = user_input.split(',')
        x, y = Casting.to_int(data[0], data[1])

    def multiply(self, x , y):
        return x * y

whichquad = input("사각형의 종류는? \n 1)평행사변형 \n 2)직사각형 \n 3)정사각형 \n")

if whichquad == 1:
  



if whichquad == 2:
    exit()

if whichquad == 3:
    exit()
