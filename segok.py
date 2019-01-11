import pymysql
import random


data = []

def read_file():
    with open("segokdong.csv", "r", encoding ='utf8') as file:
        for line in file:      
            data.append(line)
        
        print(data)


data2 = read_file()


string = "\n"

for i in data2:
    data3 = data2.replace(string, "")

print(data3)