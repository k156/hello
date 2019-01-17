from bs4 import BeautifulSoup
import requests
from time import sleep


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

url = "https://www.melon.com/chart/index.htm#params%5Bidx%5D=1/"
html = requests.get(url, headers = headers).text

soup = BeautifulSoup(html, 'html.parser')

trs = soup.select("tr#lst50")


for tr in trs:
    tds = tr.select('td')

    rank = tds[1].text
    title = tds[4]
    # singer = 

    # print(rank, title, type(title))
    
    print(rank, title, type(title))