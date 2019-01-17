from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = 'C:\workspace\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(drvPath)
<<<<<<< HEAD
UserId1 = "seno"
UserId2 = "rbur"
UserId3 = "ns"
UserPw1 = "Kim0"
UserPw2 = "5803"
UserPw3 = "158"
=======
UserId = "id"
UserPw = "pw"


>>>>>>> 6418f1b6141837524189f249c348434fe30596dc

driver.get("https://www.naver.com")
sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
<<<<<<< HEAD
print("click big button!!")
sleep(2)

id = driver.find_element_by_id('id')
for a in UserId1:
    sleep(random.randrange(1, 5) * 0.04)
    id.send_keys(a)
for b in UserId2:
    sleep(random.randrange(1, 5) * 0.06)
    id.send_keys(b)
for c in UserId3:
    sleep(random.randrange(1,5) * 0.05)
    id.send_keys(c)

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
=======

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
>>>>>>> 6418f1b6141837524189f249c348434fe30596dc

          # cf.  driver.implicitly_wait(5)
# driver.quit() # driver.close()