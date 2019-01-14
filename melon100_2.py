from bs4 import BeautifulSoup
import requests
from time import sleep


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

url = "https://www.melon.com/chart/index.htm#params%5Bidx%5D=1/"
html = requests.get(url, headers = headers).text

soup = BeautifulSoup(html, 'html.parser')

td4s = soup.select("tr#lst50 > td:nth-of-type(6)")



for td4 in td4s:

	info = td4.text
	print(info)



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






