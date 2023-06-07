import time 
from login import pim_login

def category_master_mapping(browser):
    pim_login(browser)

    #Attribute module    
    browser.find_element("xpath",'//span[contains(text(),"Attribute")]').click()
    time.sleep(5)

    #Category Master and Mapping
    browser.find_element("xpath",'//a[contains(text(),"Category Master And Mapping")]').click()
    print("Opened category mapping")
    time.sleep(5)

    #Hardware
    hardware=browser.find_element("xpath",'//span[normalize-space()="Hardware"]').click()
    print("Hardware selected")
    time.sleep(3)
    tools=browser.find_element("xpath",'//span[normalize-space()="Tools"]').click()
    print("Tools selected")
    time.sleep(3)
    Electric_tools= browser.find_element("xpath",'//input[@value="1379"]').click()
    print("electric Tools selected")
    time.sleep(3)


    #Add Attribute button

    button=browser.find_element("xpath",'//span[normalize-space()="Add Attribute"]').click()
    print("Button clicked")
    time.sleep(3)

    #Adding new attribute
    newattr=browser.find_element("xpath",'//tr[@id="1299"]//input[@type="checkbox"]').click()
    time.sleep(5)
    addbutton=browser.find_element("xpath",'//span[normalize-space()="Add"]').click()
    time.sleep(5)
    print("Attribute added")

