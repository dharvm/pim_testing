import time 
from login import pim_login

def user_create(browser):
    pim_login(browser)  
    browser.find_element("xpath",'//span[contains(text(),"System Admin")]').click()
    browser.find_element("xpath",'//a[contains(text(),"User Management")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//span[contains(text(),"Create")]').click()

    time.sleep(2)

    browser.find_element("id","user_name").send_keys("dharv_m")
    browser.find_element("id","first_name").send_keys("Dharv")
    browser.find_element("id","last_name").send_keys("Mistry")
    browser.find_element("id","email").send_keys("dharv.mistry@vinculumgroup.com")

    browser.find_element("xpath",'//span[contains(text(),"Save")]').click()
    time.sleep(2)
