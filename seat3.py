import requests


session = requests.session()

loginUrl = "http://ticket.yes24.com/OSIF/Book.asmx/GetHallMapRemainFN"
params = {
    "idHall": "8531",
    "idTime": "985109"
}

headers = {
	"referrer":"http://ticket.yes24.com/OSIF/Book.asmx?op=GetHallMapRemainFN"
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

res = session.post(loginUrl, data=params)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

print(soup)