import requests
from bs4 import BeautifulSoup

session = requests.session()

loginUrl = "https://www.yes24.com/Templates/FTLogin.aspx"

headers = {
    "Referer": 'http://ticket.yes24.com/',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

login_info = {
        'LoginType': '',
        'FBLoginSub$ReturnURL': 'http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx' ,
        'FBLoginSub$ReturnParams': 'IdPerf=32098' ,
        'RefererUrl': '', 
        'AutoLogin': '1' ,
        'LoginIDSave': 'Y' ,
        'FBLoginSub$NaverCode': '' ,
        'FBLoginSub$NaverState': '' ,
        'FBLoginSub$Facebook': '' ,
        'SMemberID': 'senorburns' ,
        'SMemberPassword': 'Kim05803158'
}

res = session.post(loginUrl, data=login_info, headers=headers)
print(\res.raise_for_status()


#접근할 페이지 1
res = session.get('http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=32098')
res.raise_for_status()

#접근할 페이지 2

page2_headers = { 'Referer': 'http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=32098' }

# page2_params = {
#     'pIdTime': '986321' ,
#     'pIdCode': '',
#     'pDisplayRemainSeat': '0'
# }

res2 =  session.get('http://ticket.yes24.com/Pages/Perf/Sale/Ajax/Perf/PerfTime.aspx',headers=page2_headers)
res2.raise_for_status()

#idHall과 idTime 추출
soup = BeautifulSoup(res2.text, "html.parser")

print(soup)

# idHall = soup.select_one('div#dBigHtmlMap')
# idTime = soup.select_one('ul#ulTime').attrs['value']