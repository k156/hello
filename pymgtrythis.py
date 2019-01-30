import requests, json
from bs4 import BeautifulSoup
from pymongo import MongoClient, DESCENDING
from pprint import pprint

url = "https://openapi.naver.com/v1/search/book.json"

title = "파이썬"
params = {
    "query": title,
    "display": 20,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "rHEoGnfNxhPls5IGSdjH",
    "X-Naver-Client-Secret": "pOjyL0OiL3"
}

# def main():
#     res = request.get(url, params = para)

res = requests.get(url, params=params, headers=headers).text
jsonData = json.loads(res)
t = jsonData['items']


for i in t:
    (int(i['price']))
    


# mongo_client = MongoClient('localhost', 27017)
# collection = mongo_client.dooodb.Songs
# result = collection.insert_many(t)
# print('Affected docs is {}'.format(len(result.inserted_ids)))



# lst = collection.find().sort('price', DESCENDING).limit(5)
# for i in lst:
#     print(i)
