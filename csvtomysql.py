import pymysql
import random
import csv, codecs


fp = codecs.open("melon_reference.csv", "r", encoding = "MS949")

reader = csv.reader(fp, delimiter=',', quotechar='"')


data = []
for cells in reader:
	data.append([cells[0], cells[1], cells[2], cells[3]])

del data[0]
del data[len(data) -1 ]

print(data)


conn = pymysql.connect(
    host='localhost',
    user='dooo',
    password='1234567',
    port=3306,
    db='dooodb',
    charset='utf8')


with conn:
	cur = conn.cursor()
	sql_truncate = "truncate table Test2"
	sql = "insert into Test2(rank, title, singer, likes) values(%s,%s,%s,%s)"
	cur.execute(sql_truncate)
	cur.executemany(sql, data)
	print("AffecedRowCount is", cur.rowcount)
	conn.commit()