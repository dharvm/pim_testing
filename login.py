import time
from wait import wait_for

def pim_login(browser):
    browser.get("https://uat-ui.vinreco.in/")
    # browser.get("http://dev2-ui.vinreco.in/")

    login_page_text = browser.find_element("xpath","/html/body/div/main/section/div/div[2]/header/div[2]/p").text

    if login_page_text == "Log in to dev-vin-auth to continue to vinculum-app.":
        print("PASS AT LOGIN")
    else:
        print("FAIL AT LOGIN")
        wait_for(5)
        

    browser.find_element("id","username").send_keys("testdemo@gmail.com")
    # browser.find_element("id","username").send_keys("pim4@gmail.com")
    browser.implicitly_wait(100)

    browser.find_element("xpath","//button[contains(text(),Continue)]").click()
    browser.implicitly_wait(100)
    time.sleep(5)


    if browser.find_element("xpath","/html/body/div/main/section/div/div/header/div[2]/p").text == "Enter your password for dev-vin-auth to continue to vinculum-app":
        print("PASS AT PASSWORD")
    else:
        print("FAIL AT PASSWORD")
        wait_for(5)
        
    browser.find_element("id","password").send_keys("Root@123")
    time.sleep(2)

    browser.find_element("xpath","/html/body/div/main/section/div/div/div/form/div[3]/button").click()
    time.sleep(2)

    browser.refresh()

    if browser.find_element("xpath","/html/body/div/div[1]/div[3]/div[1]/nav/div[1]/h5/b").text == "VIN2.0":
        print("REACHED TO DASHBOARD")
    else:
        print("FAILED TO DASHBOARD")
        wait_for(5)
        
    time.sleep(2)
      