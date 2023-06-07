import time 
import random
from login import pim_login

def product_attribute(browser):
    pim_login(browser)

    #Attribute module    
    browser.find_element("xpath",'//span[contains(text(),"Attribute")]').click()

    #Product Attribute
    browser.find_element("xpath",'//a[contains(text(),"Product Attribute")]').click()
    time.sleep(2)

    #Add New Attribute
    browser.find_element("xpath",'//span[contains(text(),"Add New Attribute")]').click()
    time.sleep(5)


    #Category dropdown
    browser.find_element("xpath", '//div[@class="mx-0 d-flex align-items-center"]').click()
    time.sleep(2)

    dropdown = browser.find_element("id",'categories-list-dropdown')  # Locate the dropdown element
    options = dropdown.find_elements("xpath",'./div[contains(@class, "col-md-12")]')  # Get all the options
    random_index = random.randint(1, len(options)-1)  # Generate a random index
    options[random_index].click()

    time.sleep(2)
    print("First dropdown passed")
    time.sleep(5)


    #Attribute group name dropdown
    browser.find_element("xpath", '//*[@id="attributeGroupName"]').click()
    time.sleep(2)

    dropdown = browser.find_element("id",'attributeGroupName')  # Locate the dropdown element



    # options1 = dropdown.find_elements("xpath",'//*[@id="attributeGroupName"]')  # Get all the options
    # options1.click()

    # random_index1 = random.randint(1, len(options1)-1)  # Generate a random index
    # options1[random_index1].click()

    browser.find_element("xpath", '//*[@id="attributeGroupName"]/option[2]').click()
    time.sleep(2)

    print("Passed second dropdown")
    time.sleep(5)


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

    #Display length
    displaylength=browser.find_element("id","length")
    displaylength.send_keys("5")
    print("Display length added")
    time.sleep(5)


    #Constraint
    browser.find_element("id", 'constraint').click()
    print("constraint selected")
    time.sleep(5)


    #Field Type
    field= browser.find_element("id",'type').click()
    time.sleep(5)
    choice=browser.find_element("xpath", '//*[@id="type"]/option[8]').click()
    print("Field type selected")
    time.sleep(5)

    #DataType
    datatype=browser.find_element("id",'dataType').click()
    time.sleep(3)
    choice1=browser.find_element("xpath",'//*[@id="dataType"]/option[5]').click()
    print('Data type added')
    time.sleep(5)

    #Rules
    mandatory=browser.find_element("id",'mandatory').click()
    time.sleep(3)
    editability=browser.find_element("id",'editability').click()
    time.sleep(3)
    default=browser.find_element("id",'default').click()
    time.sleep(3)
    value=browser.find_element("xpath",'//*[@id="addAttr"]/div/div/div[2]/form/div[2]/div[1]/div[2]/div[9]/div/div/div/div/div[3]/div[3]/input').send_keys("5")
    time.sleep(3)
    panel=browser.find_element("id",'panel').click()
    time.sleep(3)
    search=browser.find_element("id",'search').click()
    print("Rules checked")
    time.sleep(5)

    #Add new attribute
    newattr=browser.find_element("xpath",'//*[@id="addAttr"]/div/div/div[2]/form/div[2]/div[2]/div/div[2]/a').click()
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


    #Constraint
    browser.find_element("id", 'constraint').click()
    print("constraint selected again")
    time.sleep(5)


    #Field Type
    field= browser.find_element("id",'type').click()
    time.sleep(5)
    choice=browser.find_element("xpath", '//*[@id="type"]/option[8]').click()
    print("Field type selected again")
    time.sleep(5)

    #DataType
    datatype=browser.find_element("id",'dataType').click()
    time.sleep(3)
    choice1=browser.find_element("xpath",'//*[@id="dataType"]/option[5]').click()
    print('Data type added again')
    time.sleep(5)

    #Rules
    mandatory=browser.find_element("id",'mandatory').click()
    time.sleep(3)
    editability=browser.find_element("id",'editability').click()
    time.sleep(3)
    default=browser.find_element("id",'default').click()
    time.sleep(3)
    value=browser.find_element("xpath",'//*[@id="addAttr"]/div/div/div[2]/form/div[2]/div[1]/div[2]/div[9]/div/div/div/div/div[3]/div[3]/input').send_keys("5")
    time.sleep(3)
    panel=browser.find_element("id",'panel').click()
    time.sleep(3)
    search=browser.find_element("id",'search').click()
    print("Rules checked again")
    time.sleep(5)





    #Add
    add=browser.find_element("xpath",'//*[@id="addAttr"]/div/div/div[2]/form/div[2]/div[2]/div/div[2]/button').click()
    print("added")
    time.sleep(10)

  