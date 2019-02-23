<<<<<<< HEAD
import requests, json
from bs4 import BeautifulSoup
from pprint import pprint
import pymysql

url = "https://openapi.naver.com/v1/search/blog.json"

title = "파이썬"
params = {
    "query": title,
    "display": 10,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "rHEoGnfNxhPls5IGSdjH",
    "X-Naver-Client-Secret": "pOjyL0OiL3"
}

result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)

# print(json.dumps(jsonData, ensure_ascii=False, indent=2))

# sss= []

# for j in jsonData['items']:
#     title = j["title"]
#     link = j["link"]
#     bloggername = j["bloggername"]
#     postdate = j["postdate"]
#     bloggerlink = j['bloggerlink']
#     description = j['description']
#     sss.append([title, link, bloggername, postdate, bloggerlink, description])


sql_insert = "insert into new_table (title, link, bloggername, postdate, bloggerlink, description) values (%(title)s,%(link)s,%(bloggername)s,%(postdate)s,%(bloggerlink)s,%(description)s)"

def get_conn():
    return pymysql.connect(
        host='35.243.74.84',
        user='root',
        password='1234567',
        port=3306,
        db='test',
        charset='utf8')



try:
	conn = get_conn()
	conn.autocommit = False
	cur = conn.cursor()
	cur.executemany(sql_insert, jsonData)
	conn.commit()
	
except Exception as err:
	conn.rollback()
	print("Error!!", err)

finally:
	try:
		conn.close()
	except Exception as err2:
		print("Fail to connect!!", err2)
	

=======
>>>>>>> e9140d2119117fda4c87d94608b8b23778f212c8
