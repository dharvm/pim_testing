import time
import random
from login import pim_login

def channel_category(browser):
    pim_login(browser)
    browser.find_element("xpath",'//span[contains(text(),"Channel")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//a[contains(text(),"Category Channel Mapping")]').click()
    time.sleep(5)

    checkboxes = browser.find_elements("xpath", "//input[@type='checkbox']")
    category_ids = [checkbox.get_attribute("id") for checkbox in checkboxes]

    for i in range(15):
        browser.find_element("id",category_ids[random.randrange(1,len(category_ids))]).click()

    time.sleep(2)

    browser.find_element("xpath",'//span[contains(text(),"Save")]').click()

