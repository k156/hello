import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\workspace\chromedriver_win32\chromedriver.exe')  # mac or linux

driver.get("http://ticket.yes24.com/OSIF/Book.asmx?op=GetHallMapRemainFN")
time.sleep(2)

IdHall = '8531'
IdTime = '985109'

idhall = driver.find_element_by_name("idHall")
idhall.send_keys(IdHall)
idtime = driver.find_element_by_name("idTime")
idtime.send_keys(IdTime)

time.sleep(4)

idhall.submit()
idtime.submit()        # cf.  inputElement.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)

seatsleft =

# if seatsleft != 0: alarm
# sleep 적당한 간격으로 주기
# while구문안에 모든걸 넣고 하루종일 돌리기
