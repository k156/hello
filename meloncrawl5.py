from bs4 import BeautifulSoup
import requests
import re
import pymysql
from time import sleep
from pprint import pprint
import json


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


# source_url = "https://www.melon.com/chart/index.htm"
source_url = "http://vlg.berryservice.net:8099/melon/list"

html = requests.get(source_url, headers = headers)
soup = BeautifulSoup(html.text, 'html.parser')

urls = soup.select('div[class=wrap] > a[href]')
trs = soup.select('div#tb_list table tbody tr[data-song-no]')



song_id = []
album_id = []


for u in urls:
	url = u.get('href')
	sp = re.compile('goSongDetail\(\'(.*)\'.*')
	ap = re.compile('goAlbumDetail\(\'(.*)\'.*')
	sid = re.findall(sp, url)
	aid = re.findall(ap, url)	
	song_id += sid
	album_id += aid

print(song_id, album_id)



genre = []

for s in song_id:
	# surl ="https://www.melon.com/song/detail.htm?songId={}".format(s)
	surl = "http://vlg.berryservice.net:8099/melon/songdetail?songId={}".format(s)
	shtml = requests.get(surl, headers = headers)
	ssoup = BeautifulSoup(shtml.text, 'html.parser')
	g = ssoup.select_one("#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-of-type(3)").text
	genre.append(g)

print(genre)

sr = {}
songrank = []

dsinger = {}

singer_no_lst = []
singer_name_lst = []

Song= {}

song_table = []


dic = {}


song ={}
for tr in trs:
    song_no = tr.attrs['data-song-no']
    title = tr.select_one('div.ellipsis.rank01 a').text
    singers = tr.select('div.ellipsis.rank02 span a')
    singer = ",".join([a.text for a in singers])
    # for a in albums:
    #     album = a.text
    # song_table += [[song_no, title, singer]]

    song[song_no] = {'title':title, 'singer': singer}



exit()


for tr in trs:
	song_no = tr.attrs['data-song-no']
	ranking = tr.select_one('span.rank').text
	title = tr.select_one('div.ellipsis.rank01 a').text
	album = tr.select_one('div.ellipsis.rank03 > a').text
	singers = tr.select('div.ellipsis.rank02 span a')
	for singer in singers:
		singer_no = singer.get("href")
		sn = re.compile('goArtistDetail\(\'(.*)\'.*')
		singer_no2 = re.findall(sn, singer_no)[0]
		singer_no_lst.append(singer_no2)
        pirnt(singer_no_lst)
		singer_name = singer.text
		# print(singer_name)
        singer_name_lst.append(singer_name)
	Song[song_no] = {'song_no': song_no, 'title':title, 'singer': singer_name}
	dsinger[song_no] = {'singer_no': singer_no2, 'singer_name': singer_name}
	dic[song_no] = {'rank': int(ranking)}

# sss = []

# for so in Song.keys():
# 	sss.append([int(so), Song[so]['title'], Song[so]['singer']])

# print(sss)
exit()

# pprint(dsinger)



# likeUrl = "http://vlg.berryservice.net:8099/melon/likejson"
# likeParams = {
#     "contsIds": ",".join(dic.keys())
# }
# resLikecnt = requests.get(likeUrl, headers=headers, params=likeParams)
# # print(resLikecnt.url)
# jsonData = json.loads(resLikecnt.text)
# # pprint(jsonData)
# for j in jsonData['contsLike']:
# 	key = str(j['CONTSID'])
# 	songDic = dic[key]
# 	songDic['likecnt'] = j['SUMMCNT']


# result = sorted(dic.items(), key=lambda d: d[1]['ranking'])

# print(result)

# exit()



def get_conn(db):
    return pymysql.connect(
        host='35.200.103.240',
        user='root',
        password='dl014532.',
        port=3306,
        db=db,
        charset='utf8')

sql_truncate = "delete Song from Meltop"
sql_insert = "insert ignore into Song(song_no, song_name) values(%s,%s)"

sql_insert = "insert into Mel_list(url) values (%s)"
isStart = True
sql2 = 'select last_insert_id()'


try:
	conn = get_conn('melondb')
	conn.autocommit = False
	cur = conn.cursor()
	cur.executemany(sql_insert, sss)
	conn.commit()
	
except Exception as err:
	conn.rollback()
	print("Error!!", err)

finally:
	try:
		conn.close()
	except Exception as err2:
		print("Fail to connect!!", err2)
	
