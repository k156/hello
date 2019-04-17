from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from pprint import pprint



USER = ""
PASS = ""

driver = webdriver.Chrome()
# driver.implicitly_wait(3)

url = "https://ticket.melon.com/performance/index.htm?prodId=203128"
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

# driver.find_element_by_xpath('//*[@id="IMG_POP_LOGIN"]').click()
print('111')
driver.switch_to.window(driver.window_handles[0])
print('222')

driver.implicitly_wait(3)



#예매팝업창 들어간후
driver.find_element_by_xpath('//*[@id="btn_later"]').click()
