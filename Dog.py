class Dog:
    def __init__(self, name):
        self.name = name
        self.color = "Blue"
        print(self.name, "has been born.")

    def speak(self):
        print("YELP!", self.name)

    def __del__(self):
        print("Dead.")


class Puppy(Dog):
    def __init__(self, name):
        self.name = name
        print("Puppy has been born.")
    
    def wag(self):
        print("Puppy wags its tail.")

puppy = Puppy('PP')
puppy.speak()
print("Name is", puppy.name)
print("isDog", isinstance(puppy, Dog))



msg = "Message complete"
first, second = msg.split(' ')
print(first, second)

##############################################


class Dog:
    def __init__(self, name):
        self.name = name
        self.color = "Blue"
        print(self.name, "has been born.")

    def speak(self):
        print("YELP!", self.name)

    def __del__(self):
        print("Dead.")


class Puppy(Dog):
    name = "강아지"

    def __init__(self):
        self.name = "Puppy"
        self.color = "Red"
        print("QQQQ> Puppy has been born.", self.name)

    def __read_diary(self):
        print("Diary content!!!")

    def speak(self):
        self.age = 2
        print("Bow wow!", self.name)

    def wag(self):
        self.__read_diary()
        print("Puppy wags its tail.")

    def puke():
        print("Puuuuuuuukkke")

class Calc:
    def plus(a, b):
        return a + b

d = Dog('puddle')
p = Puppy()
d.speak()
p.speak()
#d.wag()
p.wag()

Puppy.puke()
#p.puke()

print("cal=", Calc.plus(1, 2)