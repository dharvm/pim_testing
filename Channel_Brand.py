import time
import random
from login import pim_login

def channel_brand(browser):
    pim_login(browser)
    browser.find_element("xpath",'//span[contains(text(),"Channel")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//a[contains(text(),"Brand Channel Mapping")]').click()
    time.sleep(5)

    browser.refresh()
    time.sleep(5)
    checkboxes = browser.find_elements("xpath", '//table//input[not(@id="checkbox") and @type="checkbox"]')

    brand_ids = [checkbox.get_attribute("id") for checkbox in checkboxes]

    print(brand_ids)
    for i in range(15):
        browser.find_element("id",brand_ids[random.randrange(1,len(brand_ids))]).click()

    time.sleep(2)

    browser.find_element("xpath",'//span[contains(text(),"Save")]').click()
