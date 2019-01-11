<<<<<<< HEAD
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\workspace\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver')  # mac or linux

driver.get("http://ticket.yes24.com/OSIF/Book.asmx/GetHallMapRemainFN")


time.sleep(2)

idhall = driver.find_element_by_name("idHall")
idhall.send_keys("8531")
idtime = driver.find_element_by_name("idTime")
idtime.send_keys("985109")

idhall.submit()
idtime.submit()        # cf.  inputElement.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit()


=======
print("a")
>>>>>>> e69e37930856563e97f7116cdffd457a6b1e6823
