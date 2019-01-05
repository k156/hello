import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

name = random.choice(fam_names) + random.choice(first_names) + random.choice(first_names)



i = 0
while (i < 101):
    i = i + 1
    print("(\'"+random.choice(fam_names) + random.choice(first_names) + random.choice(first_names)+"\',),")


