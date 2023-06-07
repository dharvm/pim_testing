import time 
import random
from selenium.webdriver.support.ui import Select
from login import pim_login

def reference_attribute(browser):
    pim_login(browser)
    #Attribute module    
    browser.find_element("xpath",'//span[contains(text(),"Attribute")]').click()

    #Reference Attribute
    browser.find_element("xpath",'//a[contains(text(),"Reference Attribute")]').click()
    time.sleep(2)

    #Add New Attribute
    browser.find_element("xpath",'//span[contains(text(),"Add New Attribute")]').click()
    time.sleep(10)

    #selecting ref master
    dropdown=browser.find_element("xpath","//select[@id='masterEntityName']")
    
    select = Select(dropdown)
    options = select.options
    options = options[1:]
    random_option = random.choice(options)
    selected_value = random_option.get_attribute("value")
    select.select_by_value(selected_value)
    
    #attribute name
    Attributename=browser.find_element("id","attributeName")
    Attributename.send_keys("sku_code")
    time.sleep(5)
    print("Added attribute name")

    #Display name
    displayname=browser.find_element("id","displayName")
    displayname.send_keys("test")
    time.sleep(5)
    print("Display name added")

    #Attribute length
    displaylength=browser.find_element("id","length")
    displaylength.send_keys("5")
    print("Display length added")
    time.sleep(5)

    #Type
    field= browser.find_element("id",'type').click()
    time.sleep(5)
    choice=browser.find_element("xpath", '//*[@id="type"]/option[6]').click()
    print("Field type selected")
    time.sleep(5)

    #Rules
    mandatory=browser.find_element("id",'mandatory').click()
    time.sleep(3)
    editability=browser.find_element("id",'editability').click()
    time.sleep(3)
    default=browser.find_element("id",'default').click()
    time.sleep(3)
    value=browser.find_element("xpath",'//*[@id="addRefAttr"]/div/div/div[2]/form/div[2]/div[1]/div[2]/div[5]/div/div/div/div/div[3]/div[3]/input').send_keys("5")
    time.sleep(3)
    panel=browser.find_element("id",'panel').click()
    time.sleep(3)
    search=browser.find_element("id",'search').click()
    print("Rules checked")
    time.sleep(5)

    #Add new attribute
    newattr=browser.find_element("xpath",'//*[@id="addRefAttr"]/div/div/div[2]/form/div[2]/div[2]/div/div[2]/a/u').click()
    print("add new attribute")
    time.sleep(5)


    #add everything again


    #attribute name
    Attributename=browser.find_element("id","attributeName")
    Attributename.send_keys("material_type")
    time.sleep(5)
    print("Added attribute name again")

    #Display name
    displayname=browser.find_element("id","displayName")
    displayname.send_keys("Material")
    time.sleep(5)
    print("Display name added again")

    #Display length
    displaylength=browser.find_element("id","length")
    displaylength.send_keys("5")
    print("Display length added again")
    time.sleep(5)

    #Field Type
    field= browser.find_element("id",'type').click()
    time.sleep(5)
    choice=browser.find_element("xpath", '//*[@id="type"]/option[8]').click()
    print("Field type selected again")
    time.sleep(5)

    #Rules
    mandatory=browser.find_element("id",'mandatory').click()
    time.sleep(3)
    editability=browser.find_element("id",'editability').click()
    time.sleep(3)
    default=browser.find_element("id",'default').click()
    time.sleep(3)
    value=browser.find_element("xpath",'//*[@id="addRefAttr"]/div/div/div[2]/form/div[2]/div[1]/div[2]/div[5]/div/div/div/div/div[3]/div[3]/input').send_keys("5")
    time.sleep(3)
    panel=browser.find_element("id",'panel').click()
    time.sleep(3)
    search=browser.find_element("id",'search').click()
    print("Rules checked again")
    time.sleep(5)

    #Add
    add=browser.find_element("xpath",'//*[@id="addRefAttr"]/div/div/div[2]/form/div[2]/div[2]/div/div[2]/button').click()
    print("added")
    time.sleep(10)
