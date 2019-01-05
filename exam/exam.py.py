#1. exam.db 만들기
import sqlite3
sqlite3
schema exam.db

#2. 학생 테이블 생성

conn = sqlite3.connect("exam.db")

with conn:
    cur = conn.cursor()
    sql = "create table Student (
	id integer primary key autoincrement not null,
	name text not null default 'name',
	grade text null,
	age text null,
	gender text null,
	addr text null,); "

    cur.execute(sql)

    conn.commit()



#3. db에 입력할 정보 불러오기
class Student:
	def __init__(self,line):
		line = (self.name, self.gender, self.age, self.score, self.addr)
		self.name = name
		self.gender = gender		
		self.age = age
		self.score = score
		self.addr = addr
    
	def __str__(self,line):
		return "({},{},{},{},{}),".format(self.name, self.score, self.age, self.gender, self.addr)


students = []
with open("students.csv", "r", encoding='utf8') as file:
	for line in (file):
		students.append(Student(line))


#DB에 정보 입력하기 


data = ( (김일수, 80, 23, 남, 서울시 노원구 중계동 123-45번지), ...)


conn = sqlite3.connect("exam.db")

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name, score, age, gender, addr) values(?,?,?,?,?)"
    cur.executemany(sql,(data))

    conn.commit()



#4. DB파일에서 정보 형식 가공하기

#4-1. 성별 알파벳으로 바꾸기

conn = sqlite3.connect("exam.db")
 
with conn:
    cur = conn.cursor()
    sql = "update Student set gender = 'F' where gender = '여', update Student set gender = 'M' where gender = '남';"
    cur.executemany(sql, (1, 10))

    conn.commit()


#4-2. 나이대로 변환하기

for i in range(9):
	(update Student set  = '{}0대' where age = 'i%' from Student;,).format(i)

conn = sqlite3.connect("exam.db")
 
with conn:
    cur = conn.cursor()
    sql = "update Student set  = '20대' where age = '2%' from Student;,"
    cur.executemany(sql, (1, 10))

    conn.commit()



#4-3. 이름 마스킹하기

conn = sqlite3.connect("exam.db")
 
with conn:
    cur = conn.cursor()
    sql = "update Student set name = '**' where 이름 두번째자의 인덱스값"
    cur.executemany(sql, (1, 10))

    conn.commit()



#4-4. 주소 자르기
 
conn = sqlite3.connect("exam.db")
 
with conn:
    cur = conn.cursor()
    sql = "update Student set addr = '' where addr like '%길%;"
    cur.executemany(sql, (1, 10))

    conn.commit()


#4-5. 성적 등급으로 바꾸기

conn = sqlite3.connect("exam.db")
 
with conn:
    cur = conn.cursor()
    sql = "update Student set grade = 'A' where addr like '9%', 
	update Student set grade = 'B' where grade like '8%', 
	update Student set grade = 'C' where grade like '7%', 
	update Student set grade = 'D' where grade like '6%', 
	update Student set grade = 'E' where max(grade) < 60;"
    cur.executemany(sql, (1, 10))

    conn.commit()




# 테이블 출력하기


with conn:
    cur = conn.cursor()
    sql = "select * from Student order by grade desc;"
    cur.execute(sql, (1, '홍길순'))
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

