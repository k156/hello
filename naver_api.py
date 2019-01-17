import requests, json
from bs4 import BeautifulSoup

url = "https://openapi.naver.com/v1/search/blog.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "id",
    "X-Naver-Client-Secret": "secret"
}

result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)

# print(json.dumps(jsonData, ensure_ascii=False, indent=2))

for j in jsonData['items']:
    print(j["title"], j["link"], j["bloggername"], j["postdate"])