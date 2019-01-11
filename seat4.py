import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

session = requests.session()



#url = "http://ticket.yes24.com/OSIF/Book.asmx/GetHallMapRemain"
url = "http://ticket.yes24.com/OSIF/Book.asmx/GetHallMapRemainFN"

headers = {
    "Referer": "http://ticket.yes24.com/OSIF/Book.asmx?op=GetHallMapRemainFN",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

params = {
    'idHall': '8531',
    'idTime': '985109'
}

res = session.post(url, data=params, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

seat_info = soup.find('regend').get_text()
split = seat_info.split('@')
print(split[4],":",split[3], split[9], ":", split[8], split[14],":", split[13])

print(split)


# if splited[3] > 0 or splited[8] > 0 or splited[13] > 0:
# 	print("say yes")
# else:
# 	print("not yet")

