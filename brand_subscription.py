import time 
import random
from login import pim_login

def brand_subscription(browser):
    pim_login(browser)
    # Subscribe
    subs=browser.find_element("xpath","//li[@id='ul-menu9']//div[@class='w-100 d-flex justify-content-between align-items-center']").click()
    print("Clicked on subscribe")
    time.sleep(5)

    #Category subscription
    catsubs=browser.find_element("xpath","//a[normalize-space()='Brand Subscription']").click()
    print("Brand subscription selected")
    time.sleep(5)


    #SubscribeBrands
    checkboxes = browser.find_elements("xpath", '(//div[@class="col-md-6"])[1]//td/../td[3]')
    category_ids = [checkbox.get_attribute("id") for checkbox in checkboxes]

    print(category_ids)
    print(len(category_ids))

    choice=category_ids[random.randrange(1,len(category_ids))]
    print(choice)

    xpath = f'//td[@id="{choice}"]/../td/input[@type="checkbox"]'
    print(xpath)
    checkbox = browser.find_element('xpath', xpath)
    checkbox.click()


    subscribe=browser.find_element("xpath",'//span[@class="akc-simple-btn-text text-uppercase "]').click()
    time.sleep(10)


    #Unsubscribe Brands
    checkboxes1 = browser.find_elements("xpath", '(//div[@class="col-md-6"])[2]//td/../td[3]')
    category_ids1 = [checkbox.get_attribute("id") for checkbox in checkboxes1]

    print(category_ids1)
    print(len(category_ids1))

    choice1=category_ids1[random.randrange(1,len(category_ids1))]
    print(choice1)


    xpath1 = f'//td[@id="{choice1}"]/../td/input[@type="checkbox"]'
    print(xpath1)
    checkbox = browser.find_element('xpath', xpath1)
    checkbox.click()

    unsubscribe=browser.find_element("xpath",'//span[@class="akc-simple-btn-text text-uppercase "]').click()
    time.sleep(5)

 


