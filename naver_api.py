import os
import sys
import urllib.request
client_id = "rHEoGnfNxhPls5IGSdjH"
client_secret = "pOjyL0OiL3"
# encText = urllib.parse.quote("파이썬") + encText 
keyword = '파이썬'
p_url = "https://openapi.naver.com/v1/search/blog?query={}&display=100&sort=date" # json 결과]
url = p_url.format(keyword.encode('utf-8'))

# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)