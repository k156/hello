import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\workspace\chromedriver_win32\chromedriver.exe')  # mac or linux

driver.get("http://m.ticket.yes24.com/Perf/Detail/PerfInfo.aspx?IdPerf=32059")
time.sleep(2)

userid = 'senorburns'
userpw = 'Kim05803158'

redbtn = driver.find_element_by_xpath('//*[@id="gd_norInfo"]/div[3]/a')
redbtn.send_keys(Keys.RETURN)

time.sleep(2)

ok = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/button/span')
ok.send_keys(Keys.RETURN)



# if seatsleft != 0: alarm
# sleep 적당한 간격으로 주기
# while구문안에 모든걸 넣고 하루종일 돌리기