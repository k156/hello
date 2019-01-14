import requests, json
from bs4 import BeautifulSoup

url = "https://openapi.naver.com/v1/search/book.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "rHEoGnfNxhPls5IGSdjH",
    "X-Naver-Client-Secret": "pOjyL0OiL3"
}

result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)

print(json.dumps(jsonData, ensure_ascii=False, indent=2))