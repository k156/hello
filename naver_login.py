from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = 'C:\workspace\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(drvPath)
UserId = "id"
UserPw = "pw"



driver.get("https://www.naver.com")
sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()

sleep(2)


driver.execute_script("document.getElementById('id').value = 'id'")
# send_keys(Keys.TAB)
driver.execute_script("document.getElementById('pw').value = 'pw'")

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
# myid.send_keys(Keys.RETURN)


# var myid = document.getElementById('id').value 
# id.send_keys(Keys.TAB)
# sleep(1)

# pw = driver.find_element_by_id('pw')
# for d in UserPw:
#     sleep(random.randrange(1, 5) * 0.03)
#     pw.send_keys(d)


# sleep(0.5)


# sleep(1)

          # cf.  driver.implicitly_wait(5)
# driver.quit() # driver.close()