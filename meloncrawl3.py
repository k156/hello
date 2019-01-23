from bs4 import BeautifulSoup
import requests
import re
import pymysql
from time import sleep


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


source_url = "https://www.melon.com/chart/index.htm"

html = requests.get(source_url, headers = headers)
soup = BeautifulSoup(html.text, 'html.parser')

urls = soup.select('div[class=wrap] > a[href]')
trs = soup.select('div#tb_list table tbody tr[data-song-no]')


song_id = []
album_id = []



def get_id(url, slist, alist):
	for u in urls:
		url = u.get('href')
		sp = re.compile('goSongDetail\(\'(.*)\'.*')
		ap = re.compile('goAlbumDetail\(\'(.*)\'.*')
		sid = re.findall(sp, url)
		aid = re.findall(ap, url)	
		slist += sid
		alist += aid

get_id(urls, song_id, album_id)


print(song_id)

genre = []

for s in song_id:
    surl ="https://www.melon.com/song/detail.htm?songId={}".format(s)
    shtml = requests.get(surl, headers = headers)
    ssoup = BeautifulSoup(shtml.text, 'html.parser')
    g = ssoup.select_one("#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-of-type(3)").text
    genre.append(g)
    sleep(2)

print(genre)

song_table = []

for tr in trs:
    song_no = tr.attrs['data-song-no']
    ranking = tr.select_one('span.rank').text
    title = tr.select_one('div.ellipsis.rank01 a').text
    singers = tr.select('div.ellipsis.rank02 span a')
    singer = ",".join([a.text for a in singers])
    album = tr.select_one('div.ellipsis.rank03 > a').text
    # for a in albums:
    #     album = a.text
    song_table += [[song_no, title, singer]]



def get_conn(db):
    return pymysql.connect(
        host='35.200.103.240',
        user='root',
        password='dooo!',
        port=3306,
        db=db,
        charset='utf8')

sql_truncate = "delete from Meltop"
sql_insert = "insert into Meltop(rank, title, singer, likecnt) values(%s,%s,%s,%s)"
isStart = True

    try:
        conn = get_conn('melondb')
	    conn.autocommit = False
        cur = conn.cursor()
        cur.executemany(sql, lst)
        conn.commit()
        
    except Exception as err:
        conn.rollback()
        print("Error!!", err)

    finally:
        try:
            conn.close()
        except Exception as err2:
            print("Fail to connect!!", err2)