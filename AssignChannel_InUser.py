import time
import random
from login import pim_login

def user_AssignChannel(browser):
    pim_login(browser)
    browser.find_element("xpath",'//span[contains(text(),"System Admin")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//a[contains(text(),"User Management")]').click()
    time.sleep(2)

    browser.find_element("xpath",'//a/u[contains(text(),"chailcy")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//ul/li/a/div[contains(text(),"Channels")]').click()
    time.sleep(2)

    assign_1st = browser.find_element("xpath",'//a/span[contains(text(),"Assign Channel")]')
   

    if assign_1st:
        assign_1st.click()
        time.sleep(2)
    elif not assign_1st:
        assign_2nd = browser.find_element("xpath",'//div[@class="card p-2 simple-btn-border mb-0 "]/a/span[contains(text(),"Assign Channel")]')
        assign_2nd.click()
        time.sleep(2)
    else:
        print("NOT ABLE TO FIND ON ASSIGN")
            
    checkboxes = browser.find_elements("xpath", '//div[@id="assignCategory"]//img/../../../div[@id]')
    category_ids = [checkbox.get_attribute("id") for checkbox in checkboxes]


    print(category_ids)
    for i in range(10):
        browser.find_element("xpath",f'//div[@id="assignCategory"]//img/../../../div[@id="{category_ids[random.randrange(1,len(category_ids))]}"]').click()

    browser.find_element("xpath",'//a/span[text()="Assign"]').click()
    time.sleep(2)

    alert_msg = browser.find_element("xpath",'//div[@class="Toastify"]/div/div/div/div[2]').text
    print("ALERT_MESSAGE after UN-ASSIGN ---> ",alert_msg)
    time.sleep(3)
    browser.refresh()
