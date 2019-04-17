from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from pprint import pprint

drvPath = 'C:\workspace\chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(drvPath)




USER = "senorburns"
PASS = "Kim05803158"

# driver = webdriver.Chrome()
# driver.implicitly_wait(3)


url = "https://ticket.melon.com/performance/index.htm?prodId=203038"
driver.get(url)

driver.find_element_by_xpath('//*[@id="list_date"]/li[1]/button/span').click()
driver.find_element_by_xpath('//*[@id="ticketing_process_box"]/div/div[2]/div/div[2]/button').click()

driver.switch_to.window(driver.window_handles[1])

i = driver.find_element_by_xpath('//*[@id="id"]')
i.clear()
i.send_keys(USER)
i = driver.find_element_by_xpath('//*[@id="pwd"]')
i.clear()
i.send_keys(PASS)

driver.find_element_by_id('IMG_POP_LOGIN').click()

# driver.find_element_by_xpath('//*[@id="IMG_POP_LOGIN"]').click()
print('111')
driver.switch_to.window(driver.window_handles[0])
print('222')

# 바꾸기
driver.find_element_by_xpath('//*[@id="list_date"]/li[2]/button/span').click()
print("date")
driver.find_element_by_xpath('//*[@id="list_time"]/li/button/span').click()
print("time")

# 예매하기 버튼
driver.find_element_by_xpath('//*[@id="ticketing_process_box"]/div/div[2]/div/div[2]/button').click()
print('book')

# 좌석 창 띄우기
# driver.switch_to.frame(driver.find_element_by_id("oneStopFrame"))
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

sleep(3)


standa = driver.find_element_by_xpath('//*[@id="iez_canvas"]/svg/rect[21]')
if standa:
    standa.click()

# ul = soup.select_one('tbody tr.box_list_area').text
# for li in ul:
#     if '0' in ul.select_one('li10032FloorA').text:
#         continue
#     else: 

standb = driver.find_element_by_xpath('//*[@id="gd10365"]/td[4]')
if standb:
    standb.click()

firstc2 = driver.find_element_by_xpath('//*[@id="ez_canvas_zone"]/svg/rect[13]')
if firstc2:
    firstc2.click()

secondc2 = driver.find_element_by_xpath('//*[@id="ez_canvas_zone"]/svg/rect[16]')
if secondc2:
    secondc2.click()
# -------------------------------------------------------------------------------
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
seatlists = soup.select('tbody#divGradeSummary tr.box_list_area div.list_area.listOn ul li')
for seat in seatlists:
    liid = seat.get('li')
    leftseats = seat.select('span.seat_residual strong')
    for l in leftseats:
        seatnum = l.text
        if seatnum != str(0):
            driver.find_element_by_id(liid).click()

canvas = soup.select('div#ez_canvas rect[fill]')
for c, idx in enumerate(canvas):
    attrs = driver.find_element_by_tag_name('rect')
    for a in attrs:
        available = c.get('fill')
        if available == '#9486f8':
            y = c.get('y') 
            if float(y) <= 715.36:
                x = c.get('x')
                x = max(x)
                # 좌석 선택
                driver.find_element_by_xpath('//*[@id="ez_canvas"]/svg/rect[{}]'.format(idx-2)).click()


# 1137에 가장 가깝게 
# #좌석 선택하기
# browser.switch_to.frame(browser.find_element_by_name("ifrmSeatFrame"))
# sleep(1)
# html = browser.page_source
# soup = BeautifulSoup(html, 'html.parser')
# empty_seats = soup.select('div#divSeatArray div[title]')
# front_seat = empty_seats[0]
# sid = front_seat.attrs['id']
# sleep(1)
# browser.find_element_by_id(sid).click()
# browser.find_element_by_class_name('booking').click()
# print("좌석선택완료")

# url = 'https://ticket.melon.com/reservation/popup/onestop.htm'
# headers = {
#     'Referer' : 'https://ticket.melon.com/performance/index.htm?prodId=203038'
# }
# res = requests.post(url, headers = headers)
# html = res.text
# soup = BeautifulSoup(html, "html.parser")
# canvas = soup.select('div#ez_canvas rect[fill]')
# for c in canvas:
#     available = c.get('fill')
#     if available == '#9486f8':
#         y = c.get('y') 
#         if y <= '663.36':
#             # 좌석 선택
#             driver.find_element_by_





# standc = driver.find_element_by_xpath('//*[@id="gd10366"]/td[4]')
# if standc:
#     standc.click()


# 선택 가능한 좌석 fill = "#9486f8" (체크 필수)
#if get('fill') == '#9486f8':
    # click()
# 870.9 =< x <= 1377.9

# 520.36=< y <=780.36


# <li id="li103651B2" onclick="selectedBlock(this,'65','1,B2','1','층','B2','구역','SE0001');" onmouseover="viewGradeZone('1,B2')" onmouseout="viewLastGradeZone()" class="ck"><span class="area_tit">1 층 B2 구역</span><span class="seat_residual"> <strong>1</strong>석</span></li>

#<rect x="731.91" y="1105.75" width="11" height="11" rx="0" ry="0" fill="#9486f8" stroke="#000" stroke-width="0" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect>

# 좌석 선택 완료 버튼
driver.find_element_by_xpath('//*[@id="nextTicketSelection"]').click()

# 다음
driver.find_element_by_xpath('//*[@id="nextPayment"]').click()

#주문자 정보와 동일
driver.find_element_by_xpath('//*[@id="copyDelvyAddr"]').click

#우편 번호
driver.find_element_by_xpath('//*[@id="btnSearchAddress"]').click

#화면 전환
driver.switch_to.window(driver.window_handles[1])

# 찾아서 입력하기

#검색

driver.find_element_by_xpath('//*[@id="searchAddressPopup"]/div[2]/div/div/div[1]/div/button').click
postzip = driver.find_element_by_xpath('//*[@id="searchWord1"]')
postzip.clear()
postzip.send_keys('중계로 233')
driver.find_element_by_xpath('//*[@id="resultTbody"]/tr/td[1]/a')
detailadd = driver.find_element_by_xpath('//*[@id="delvyAddrDtl"]')
detailadd.clear()
detailadd.send_keys('103-803')


#무통장 입금
driver.find_element_by_xpath('//*[@id="payMethodCode003"]').click()

# 은행 선택 (질문)
driver.find_element_by_xpath('//*[@id="partPaymentVbank"]/div/table/tbody/tr[1]/td/div/div/select').click()

# 국민은행
driver.find_element_by_xpath('//*[@id="partPaymentVbank"]/div/table/tbody/tr[1]/td/div/div/select/option[3]').click()

# 휴대폰 번호
ph_1 = '5424'
frontph = driver.find_element_by_xpath('//*[@id="cashReceiptRegTelNo2"]')
frontph.clear()
frontph.send_keys(ph_1)

ph_2 = '7836'
frontph = driver.find_element_by_xpath('//*[@id="cashReceiptRegTelNo3"]')
frontph.clear()
frontph.send_keys(ph_2)

# 전체 동의
driver.find_element_by_xpath('//*[@id="chkAgreeAll"]').click()

# 결제하기
driver.find_element_by_xpath('//*[@id="btnFinalPayment"]').click()