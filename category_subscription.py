import time 
import random
from login import pim_login
def category_subscription(browser):
    pim_login(browser)


    # Subscribe
    subs=browser.find_element("xpath","//li[@id='ul-menu9']//div[@class='w-100 d-flex justify-content-between align-items-center']").click()
    print("Clicked on subscribe")
    time.sleep(5)

    #Category subscription
    catsubs=browser.find_element("xpath","//a[normalize-space()='Category Subscription']").click()
    print("category subscription selected")
    time.sleep(5)

    #Selecting random values from the table


    checkboxes = browser.find_elements("xpath", '//td/../td[3]')
    category_ids = [checkbox.get_attribute("id") for checkbox in checkboxes]

    print(category_ids)
    print(len(category_ids))

    print(category_ids[random.randrange(1,len(category_ids))])
    # for i in range(15):
    #     browser.find_element('xpath',f'//td[@id="{category_ids[random.randrange(1,len(category_ids))]}"]/../td/input["checkbox"]').click()
        
    # Generate a list of three unique random indices
    random_indices = random.sample(range(len(category_ids)), 3)

    for index in random_indices:
        category_id = category_ids[index]
        xpath = f'//td[@id="{category_id}"]/../td/input[@type="checkbox"]'
        checkbox = browser.find_element('xpath', xpath)
        checkbox.click()

