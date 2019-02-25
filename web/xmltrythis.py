import csv, codecs
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
	singer = info.select('div.rank02 a')
	# print(song_no, rank, title, singer)
	# print("--------------------------")
	dic[song_no] = {"rank": rank, "title": title, "singer" : singer}

# pprint.pprint(dic)
# print(",".join(list(dic.keys())))

params = {
	"contsIds": ",".join(list(dic.keys()))
}

jsonRes = requests.get(lurl, headers = headers, params=params)
# print(jsonRes.url)


jsonData = json.loads(jsonRes.text)
# print(json.dumps(jsonData, ensure_ascii=False, indent=2))

for j in jsonData['contsLike']:
	contsid = j['CONTSID']
	likecnt = j['SUMMCNT']
	# print(contsid, likecnt)
	dic[str(contsid)]['likecnt'] = likecnt


pprint.pprint(dic)


liked = sorted(dic.items(), key=lambda d: d[1]['likecnt'])
leastliked = liked[0][1]['likecnt']



with codecs.open('melontop100.csv', 'w', 'utf-8') as ff:
	writer = csv.writer(ff, delimiter=',', quotechar='"')
	writer.writerow(['랭킹', '제목', '가수명', '좋아요수', '좋아요 차이'])
	
	likesum = 0
	diffsum = 0

	for i in dic.items():
		rank = i[1]['rank']
		title = i[1]['title']
		singer = i[1]['singer']
		likes = i[1]['likecnt']
		diff = i[1]['likecnt'] - leastliked
		l = [rank,title,singer,likes,diff]
		writer.writerow(l)
		likesum = likesum + likes
		diffsum = diffsum + diff

	writer.writerow(['계','','',likesum, diffsum])