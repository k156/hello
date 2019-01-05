import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

name = random.choice(fam_names) + random.choice(first_names) + random.choice(first_names)


city = ["서울시","부산시","울산시","대구시","광주시","인천시"]
address = list("강남개포송파홍대강서노원안암화곡대치가나다라마바사아자차카타파하")

number = list("0123456789")


a = [random.choice(fam_names) + random.choice(first_names) + random.choice(first_names), random.choice(city)+' '+ random.choice(address)+random.choice(address)+'구 '+ random.choice(address)+random.choice(address)+'동 '+ str(random.randrange(1,100))+'-'+ str(random.randrange(1,100)]
print(a)
