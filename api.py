import requests, json
from bs4 import BeautifulSoup
from pprint import pprint
import re
import pymysql

url = "https://openapi.naver.com/v1/search/blog.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "rHEoGnfNxhPls5IGSdjH",
    "X-Naver-Client-Secret": "secret"
}

result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)



p1 = re.compile('com/(.*)')
p2 = re.compile('.*//(.*)\.com.*')

# bids = []
# blogger = []
# blogpost = []

# for j in jsonData['items']:
#     link = j['bloggerlink']
#     bid = re.findall (p1, link)
#     if len(bid) == 0:
#         bid = re.findall (p2, link)
#         bid = bid[0]
#         bids.append(bid)
#     else:
#         bid = bid[0]
#         bids.append(bid)
#     name = j['bloggername']
#     blogger.append([title, bid, name, link])

#     title = j['title']
#     url = j['link']
#     postdt = j['postdate']
#     blogpost.append([title, url, bid, postdt])




blogger = {}
blogpost = {}

for j in jsonData['items']:
    title = j['title']
    link = j['bloggerlink']
    bid = re.findall (p1, link)
    if len(bid) == 0:
        bid = re.findall (p2, link)
        bid = bid[0]
    else:
        bid = bid[0]
    name = j['bloggername']
    url = j['link']
    postdt = j['postdate']
    blogger[bid] = {'id' :bid, 'name' : name, 'link': link}
    blogpost[bid] = {'title' : title, 'url': url, 'id' : bid, 'postdt': postdt}
print(blogger)
print(blogpost)



sql_blogger = '''insert ignore into Blogger(id, name, link) values (%(id)s, %(name)s, %(link)s)'''
sql_blogpost = '''insert into BlogPost (title, url, bloggerid, rgdt) values(%(title)s, %(url)s, %(id)s, %(postdt)s)'''

def get_conn(db):
    return pymysql.connect(
    host='35.243.74.84',
    user='root',
    password='1234567',
    port=3306,
    db=db,
    charset='utf8')

isStart = True

try:
    conn = get_conn('melondb')
    conn.autocommit = False
    cur = conn.cursor()
    for bl in blogger:
        cur.execute(sql_blogger, bl)
    conn.commit()

except Exception as err:
    conn.rollback()
    print("Error!!", err)

finally:
    try:
        conn.close()
    except Exception as err2:
        print("Fail to connect!!", err2)