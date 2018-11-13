def write_file():
    with open("a.csv", "w", encoding ='utf8') as file:
        file.write("이름,성별,나이 \n")
        file.write("김정민,여,28 \n")
        file.write("김남윤,남,24 \n")
        file.write("김나온,남,29")

def read_file():
    with open("a.csv", "r", encoding ='utf8') as file:
        for line in file:
            print(line)


write_file()
read_file()