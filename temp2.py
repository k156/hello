  class Paral:
    def __init__(self, name):
        self.name = name

    def question(self, answer):
        length = input("양 변의 길이를 입력하시오. ex) 3,4 ")

    def split(self, length):
        a, b = length.split(',')

    def integer(self, a, b):
        x, y = int(a), int(b)

    def multiply(self, x , y):
        return x * y

whichquad = input("사각형의 종류는? \n 1)평행사변형 \n 2)직사각형 \n 3)정사각형 \n")

if whichquad == 1:
    paral = Paral("평행사변형")
    paral.question()
    paral.split()
    paral.integer()
    paral.multiply()



if whichquad == 2:
    exit()

if whichquad == 3:
    exit()

    
    
    
    
     def outmsg():
        r = self.multiply()
        print(self.name"의 면적 = ", r)





============================================

    

class Rec(Paral):
    na=1

class Square(Paral):
    na =2



paral = Paral("평행사변형")
paral.multiply(5, 2)


print(rec.multiply(3, 4))
paral = Paral("평행")
print(paral.multiply(2,5))
rec = Rec("사각")

