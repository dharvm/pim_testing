import time
import random
from login import pim_login

def user_AssignRole(browser):
    pim_login(browser)
    browser.find_element("xpath",'//span[contains(text(),"System Admin")]').click()
    browser.find_element("xpath",'//a[contains(text(),"User Management")]').click()
    time.sleep(2)

    browser.find_element("xpath",'//a/u[contains(text(),"chailcy")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//a/div[contains(text(),"Roles")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//a/span[contains(text(),"Assign Role")]').click()
    time.sleep(2)


    checkboxes = browser.find_elements("xpath", '//div[@id="assignCategory"]//tr[@id]')
    role_ids = [checkbox.get_attribute("id") for checkbox in checkboxes]

    print(role_ids)
    for i in range(15):
        browser.find_element("xpath",f'//div[@id="assignRole"]//tr[@id="{role_ids[random.randrange(1,len(role_ids))]}"]/td/input[@type="checkbox"]').click()


    browser.find_element("xpath",'//a/span[text()="Assign"]').click()
    time.sleep(5)
