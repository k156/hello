from bs4 import BeautifulSoup
import requests
import re

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

source_url = "https://www.melon.com/chart/index.htm"

html = requests.get(source_url, headers = headers)
soup = BeautifulSoup(html.text, 'html.parser')

urls = soup.select('div[class=wrap] > a[href]')


song_id = []
album_id = []



def get_id(url, slist, alist):
	for u in urls:
		url = u.get('href')
		sp = re.compile('goSongDetail\(\'(.*)\'.*')
		ap = re.compile('goAlbumDetail\(\'(.*)\'.*')
		sid = re.findall(sp, url)
		aid = re.findall(ap, url)	
		slist += aid
		alist += sid

get_id(urls, song_id, album_id)

print(song_id, album_id)



