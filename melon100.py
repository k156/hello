from bs4 import BeautifulSoup
import requests
import json
from time import sleep
import pprint


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

url = "https://www.melon.com/chart/index.htm"
lurl = "https://www.melon.com/commonlike/getSongLike.json"

htmlRes = requests.get(url, headers = headers)
print("HTML>>>>", htmlRes.url)
soup = BeautifulSoup(htmlRes.text, 'html.parser')
trs = soup.select('tr[data-song-no]')

dic = {}
for tr in trs:
	song_no = tr.attrs['data-song-no']
	rank = tr.select_one('td span.rank').text
	info = tr.select_one('div.wrap_song_info')
	title = info.select_one('div.rank01 a').text
	singer = info.select_one('div.rank02 a').text
	# print(song_no, rank, title, singer)
	# print("--------------------------")
	dic[song_no] = {"rank": rank, "title": title, "singer" : singer}

# pprint.pprint(dic)
# print(",".join(list(dic.keys())))

params = {
	"contsIds": ",".join(list(dic.keys()))
}

jsonRes = requests.get(lurl, headers = headers, params=params)
print(jsonRes.url)
jsonData = json.loads(jsonRes.text)
# print(json.dumps(jsonData, ensure_ascii=False, indent=2))

for j in jsonData['contsLike']:
	contsid = j['CONTSID']
	likecnt = j['SUMMCNT']
	print(contsid, likecnt)
	dic[str(contsid)]['likecnt'] = likecnt


pprint.pprint(dic)


# html = requests.get(url, headers = headers).text
# result = requests.get(lurl, headers=headers, params = params).text


# print("result", result)
# # jsonData = json.loads(result)


# soup = BeautifulSoup(html, 'html.parser')

# trs = soup.select("tr#lst50")
# td4s = soup.select("tr#lst50 > td:nth-of-type(6)")
# likecnt = soup.select("#lst50 > td:nth-of-type(8) > div > button > span.cnt")


# for tr in trs:
# 	tds = tr.select('td')
# 	rank = tds[1].text
# 	# print(rank)


# for	td4 in td4s:
# 	info = td4.text
# 	# print(info)


# dic = {}

