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
trs2 = soup.select("tr#lst100")
likes = soup.select("#lst50 > td:nth-of-type(8) > div > button > span.cnt")

for tr in trs:

	tds = tr.select('td')
	rank = tds[1].text
	td4s = tr.select('td:nth-of-type(5)')
	for td in td4s:
		titles = td.attrs['title']
		print(titles)

	# info = tds[4].attrs['title']

	# singer = tds[5]

    # print(rank, title, type(title))


	# print(info)
# 	print(rank, info)




	# a = tr.select('a[href]')
	# for i in a:
	# 	titles = i.attrs['title']
	# 	print(titles)



# for tr in trs2:
# 	tds = tr.select('td')

# 	rank = tds[1].text
# 	info = tds[4].next_sibling.next_sibling.text
    
# 	print(rank, info)

