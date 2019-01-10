from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/marketindex/exchangeList.nhn"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

buy = soup.select("table[class=tbl_exchange] > tbody > tr > td:nth-of-type(3)")
sell = soup.select("table[class=tbl_exchange] > tbody > tr > td:nth-of-type(4)")


buy_list = []
for i in buy:
	buy_value = i.text
	buy_value = float(buy_value.replace(",",""))
	buy_list.append(buy_value)
print(buy_list, type(buy_list))


sell_list = []
for i in sell:
	sell_value = i.text
	sell_value = float(sell_value.replace(",",""))
	sell_list.append(sell_value)

print(sell_list, type(sell_list))


dif = []

for i in range(0, 44):
	# print(i, buy_list[i], sell_list[i])
	difference = round(buy_list[i] - sell_list[i])
	dif.append(difference)
print("dif>>>", dif)
