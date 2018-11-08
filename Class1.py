whichQuad = input("사각형의 종류는? \n 1)평행사변형 \n 2)직사각형 \n 3)정사각형")
if WhichQuad = 1:
    length = input("양 변의 길이를 입력하시오. ex) 3, 4 ")
    
paral = Paral("평행사변형")
paral.multiply(5, 2) 




class Paral():
    def __init__(self, name):
        self.name = name

    def multiply(self, a, b):
        return a * b

    def outmsg(self, r):
        r = multiply()
        print(self.name"의 면적은 {}입니다.".format(r))
    

class Rec(Paral):
    na=1

class Square(Paral):
    na =2



print(rec.multiply(3, 4))
paral = Paral("평행")
print(paral.multiply(2,5))
rec = Rec("사각")

