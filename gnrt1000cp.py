import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

name = random.choice(fam_names) + random.choice(first_names) + random.choice(first_names)


city = ["서울시","부산시","울산시","대구시","광주시","인천시"]
address = list("강남개포송파홍대강서노원안암화곡대치가나다라마바사아자차카타파하")

number = list("0123456789" * 3)

years = ['1931',
'1932',
'1933',
'1934',
'1935',
'1936',
'1937',
'1938',
'1939',
'1940',
'1941',
'1942',
'1943',
'1944',
'1945',
'1946',
'1947',
'1948',
'1949',
'1950',
'1951',
'1952',
'1953',
'1954',
'1955',
'1956',
'1957',
'1958',
'1959',
'1960',
'1961',
'1962',
'1963',
'1964',
'1965',
'1966',
'1967',
'1968',
'1969',
'1970',
'1971',
'1972',
'1973',
'1974',
'1975',
'1976',
'1977',
'1978',
'1979',
'1980',
'1981',
'1982',
'1983',
'1984',
'1985',
'1986',
'1987',
'1988',
'1989',
'1990',
'1991',
'1992',
'1993',
'1994',
'1995',
'1996',
'1997',
'1998',
'1999',
'2000',
'2001',
'2002',
'2003',
'2004',
'2005',
'2006',
'2007',
'2008',
'2009',
'2010']

months = ['01','02','03','04','05','06','07','08','09','10','11','12']

days = ['01',
'02',
'03',
'04',
'05',
'06',
'07',
'08',
'09',
'10',
'11',
'12',
'13',
'14',
'15',
'16',
'17',
'18',
'19',
'20',
'21',
'22',
'23',
'24',
'25',
'26',
'27',
'28',
'29',
'30',
'31']


domains = ['@outlook.com', '@gmail.com', '@hotmail.com', '@naver.com','@daum.net','@hotmail.co.kr']

atoz = list('abcdefghijklmnopqrstuvwxyz' * 3)


    a = [random.choice(fam_names) + random.choice(first_names) + random.choice(first_names), random.choice(city)+' '+ random.choice(address)+random.choice(address)+'구 '+ random.choice(address)+random.choice(address)+'동 '+ str(random.randrange(1,100))+'-'+ str(random.randrange(1,100))]
    b = [random.choice(years)+'-'+random.choice(months)+'-'+random.choice(days), '010-'+ random.choice(number)+random.choice(number)+random.choice(number)+random.choice(number)+'-'+ random.choice(number)+random.choice(number)+random.choice(number)+random.choice(number)]
    c = [random.choice(atoz) + random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) + str(random.randrange(0,9)) + str(random.randrange(0,9))+ str(random.randrange(0,9)) + random.choice(domains)]
    d = [random.choice(atoz) + random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) + str(random.randrange(0,9)) + str(random.randrange(0,9))+ str(random.randrange(0,9)) + random.choice(domains)+',']
    e = [random.choice(atoz) + random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) + str(random.randrange(0,9)) + str(random.randrange(0,9)) + str(random.randrange(0,9))+ str(random.randrange(0,9)) + random.choice(domains)+',']

    return a+b+c


#이름, 주소 생년월일, 전화번호 QQQ. 2월은 28일까지
i = 0
while (i < 11):
    


#이메일

# i = 0
# while (i < 21):
#     i += 1
#     print(c)


# i = 0
# while (i < 21):
#     i += 1
   

# i = 0
# while (i < 21):
#     i += 1
   

# i = 0
# while (i < 21):
#     i += 1
#     f= random.choice(atoz) + random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) + str(random.randrange(0,9)) + str(random.randrange(0,9)) + str(random.randrange(0,9)) + str(random.randrange(0,9))+ str(random.randrange(0,9)) + random.choice(domains)+','

# i = 0
# while (i < 21):
#     i += 1
#     g= random.choice(atoz) + random.choice(atoz) + random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) +random.choice(atoz) + str(random.randrange(0,9)) + str(random.randrange(0,9)) + str(random.randrange(0,9))+ str(random.randrange(0,9)) + random.choice(domains)+','





# i = 0
# j = j = 1930
# while (i < 80):
#     j += 1
#     i += 1
#     print("\'"+str(j)+"\',")

# i = 0
# j = j = 0
# while (i < 30):
#     j += 1
#     i += 1
#     print("\'"+str(j)+"\',")
    

