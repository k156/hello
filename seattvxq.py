from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from pprint import pprint

# def split(_seat):
# 	seat_list = _seat.split('^')
# 	seats = []
# 	for i in seat_list:
# 		real_seat_list = i.split('@')
# 		seats.append(real_seat_list)
# 	return seats




# session = requests.session()

# #url = "http://ticket.yes24.com/OSIF/Book.asmx/GetHallMapRemain"
# url = "http://ticket.yes24.com/OSIF/Book.asmx/GetHallMapRemainFN"

# headers = {
#    "Referer": "http://ticket.yes24.com/OSIF/Book.asmx?op=GetHallMapRemainFN",
#    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
# }

# params = {
#    'idHall': '8531',
#    'idTime': '985109'
# }

# res = session.post(url, data=params, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "html.parser")

# seat_info = soup.find('regend').get_text()
# seat_info2 = soup.find('section').get_text()

# # print(seat_info2)

# # tm.split_1(seat_info)
# print("--------------")

# split(seat_info2)

# print(seats[0][2])


# area = '빈 자리 있는 area'

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
# 	"referrer":"http://ticket.yes24.com/OSIF/Book.asmx/GetBookWhole"
# }


#셀레늄 써서 예사 로그인

USER = "senorburns"
PASS = "Kim05803158"

browser = webdriver.Chrome()
browser.implicitly_wait(3)

# 로그인 페이지에 접근하기. 
url_login = "https://www.yes24.com/Templates/FTLogin.aspx?ReturnURL=http://ticket.yes24.com/Pages/Perf/Detail/Detail.aspx&&ReturnParams=IdPerf=30862"

browser.get(url_login)
print("로그인 페이지에 접근합니다.")

# 아이디와 비밀번호 입력하기.
e = browser.find_element_by_id("SMemberID")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("SMemberPassword")
e.clear()
e.send_keys(PASS)

# 입력 양식 전송해서 로그인하기.
form = browser.find_element_by_css_selector("button#btnLogin").submit()
print("로그인 버튼을 클릭합니다.")

# 예매버튼 클릭.
reserve_bt = browser.find_element_by_class_name("rbt_reserve").click()
print("예매 버튼을 클릭합니다.")

# 팝업 창으로 전환.
browser.switch_to.window(browser.window_handles[1])

# 날짜 선택하기(26일)
date_sel = browser.find_element_by_id("2019-01-27").click()
sleep(1)

# '좌석선택' 버튼 클릭.
res = browser.find_element_by_css_selector("div.fr img").click()

#좌석 선택하기
browser.switch_to.frame(browser.find_element_by_name("ifrmSeatFrame"))
sleep(1)
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')
empty_seats = soup.select('div#divSeatArray div[title]')
front_seat = empty_seats[0]


sid = front_seat.attrs['id']
sleep(1)
browser.find_element_by_id(sid).click()
browser.find_element_by_class_name('booking').click()
print("좌석선택완료")

browser.switch_to_default_content()
print("다시원래창으로 돌아옴")

browser.find_element_by_xpath('//*[@id="StepCtrlBtn03"]/a[2]/img').click()
print("할인쿠폰 다음버튼")
sleep(2)

browser.find_element_by_xpath('//*[@id="StepCtrlBtn04"]/a[2]/img').click()
browser.find_element_by_id('rdoPays22').click()
browser.find_element_by_xpath('//*[@id="selBank"]/option[5]').click()
browser.find_element_by_xpath('//*[@id="cbxCancelFeeAgree"]').click()
browser.find_element_by_xpath('//*[@id="chkinfoAgree"]').click()
pic = browser.save_screenshot("pic.png")
# browser.find_element_by_xpath('//*[@id="imgPayEnd"]').click()