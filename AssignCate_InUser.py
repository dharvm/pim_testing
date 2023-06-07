import time
import random
from login import pim_login

def user_AssignCategory(browser):
    pim_login(browser)
    browser.find_element("xpath",'//span[contains(text(),"System Admin")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//a[contains(text(),"User Management")]').click()
    time.sleep(2)

    browser.find_element("xpath",'//a/u[contains(text(),"chailcy")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//ul/li/a/div[contains(text(),"Category")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//a/span[contains(text(),"Assign Category")]').click()
    time.sleep(2)

    checkboxes = browser.find_elements("xpath", '//div[@id="assignCategory"]//tr[@id]')
    category_ids = [checkbox.get_attribute("id") for checkbox in checkboxes]

    # print(category_ids)
    for i in range(15):
        browser.find_element("xpath",f'//div[@id="assignCategory"]//tr[@id="{category_ids[random.randrange(1,len(category_ids))]}"]/td/input[@type="checkbox"]').click()

    browser.find_element("xpath",'//a/span[text()="Assign"]').click()
    time.sleep(2)

    alert_msg = browser.find_element("xpath",'//div[@class="Toastify"]/div/div/div/div[2]').text
    print("ALERT_MESSAGE after ASSIGN ---> ",alert_msg)
    time.sleep(3)
    browser.refresh()   
    # for alert path = //div[@class="Toastify"]/div/div/div/div[2]
                        # //div[@class="Toastify"]/div/div/div/div[2]/following::text()

    checkboxes = browser.find_elements("xpath", '//div[@id="assignCategory"]//tr[@id]')
    category_ids_2 = [checkbox.get_attribute("id") for checkbox in checkboxes]

    # print(category_ids_2)
    for i in range(15):
        browser.find_element("xpath",f'//div[@id="assignCategory"]//tr[@id="{category_ids_2[random.randrange(1,len(category_ids_2))]}"]/td/input[@type="checkbox"]').click()

    browser.find_element("xpath",'//a/span[contains(text(),"Unassign")]').click()
    time.sleep(2)

    alert_msg = browser.find_element("xpath",'//div[@class="Toastify"]/div/div/div/div[2]').text
    print("ALERT_MESSAGE after UN-ASSIGN ---> ",alert_msg)
    time.sleep(3)
    browser.refresh() 