from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = 'C:\workspace\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(drvPath)
UserId = ""
UserPw = ""

driver.get("https://www.naver.com")
sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
print("click big button!!")
sleep(2)


sleep(0.5)

id.send_keys(Keys.TAB)
sleep(1)

pw = driver.find_element_by_id('pw')
for d in UserPw1:
    sleep(random.randrange(1, 5) * 0.03)
    pw.send_keys(d)
for e in UserPw2:
    sleep(random.randrange(1, 5) * 0.04)
    pw.send_keys(e)
for f in UserPw3:
    sleep(random.randrange(1, 5) * 0.07)
    pw.send_keys(f)

sleep(0.5)
pw.send_keys(Keys.RETURN)

sleep(1)

          # cf.  driver.implicitly_wait(5)
# driver.quit() # driver.close()