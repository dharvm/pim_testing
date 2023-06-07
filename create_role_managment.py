import time
from login import pim_login

def role_create(browser):
    pim_login(browser)
    browser.find_element("xpath",'//span[contains(text(),"System Admin")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//a[contains(text(),"Role Management")]').click()
    time.sleep(5)
    browser.find_element("xpath",'//span[contains(text(),"Create")]').click()

    time.sleep(2)
    browser.find_element("id","role_name").send_keys("Dharv")

    # code to create role in lister -> Application -> create

    # browser.find_element("xpath",'//input[@value="Lister"]').click()
    # time.sleep(1)
    # browser.find_element("xpath",'//input[@value="Application"]').click()
    # time.sleep(1)


    # code to create role in PIM -> Workflow -> Initiator/Reviewer/Approver -> create
    browser.find_element("xpath",'//input[@value="Pim"]').click()
    time.sleep(1)
    browser.find_element("xpath",'//input[@value="Workflow"]').click()
    time.sleep(1)
    browser.find_element("xpath",'//input[@value="initiator"]').click()
    time.sleep(1)
    # browser.find_element("xpath",'//span[@class="slider round"]').click() 
    # time.sleep(1)
    browser.find_element("name","role_desc").send_keys("testing lister application active status decs")

    browser.find_element("xpath",'//span[contains(text(),"Save")]').click() 
    time.sleep(2)


