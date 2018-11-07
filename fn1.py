cal = input("식을 입력하시오. ex)a + b ")
cals = cal.strip().split(' ')

a = int(cals[0])
b = int(cals[2])
op = cals[1]

if op == "+":
    def plus(a,b):
        return a + b
    r = plus(a,b)
    print("정답은", r)

if op == "-":
    def minus(a,b):
        return a - b
    e = minus(a,b)
    print("정답은", e)

if op == "*":
    def multiply(a,b):
        return a * b
    w = multiply(a,b)
    print("정답은", w)

if op == "/":
    def divide(a,b):
        return a / b
    q = divide(a,b)
    print("정답은", q)


    