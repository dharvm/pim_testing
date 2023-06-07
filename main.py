from login import pim_login
from create_user import user_create
from create_role_managment import role_create
from AssignRole_InUser import user_AssignRole
from AssignCate_InUser import user_AssignCategory
from AssignChannel_InUser import user_AssignChannel
from Channel_Brand import channel_brand
from Channel_category import channel_category
from Channel_Mapping import channel_mapping

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.maximize_window()


# pim_login(browser) # for login to PIM Dashboard

#---------------------SYSTEM ADMIN-----------------------
# user_create(browser)  # for creating new user
# role_create(browser)  # for creating new role
# user_AssignRole(browser)  # to assign role to user
# user_AssignCategory(browser)  # to assign category in user
# user_AssignChannel(browser)  # to assign channel in user

#------------------------CHANNEL-------------------------
# channel_category(browser)  # channel -> category Channel Mapping
# channel_brand(browser)  # channel -> Brand Channel Mapping
# channel_mapping(browser) # channel -> Mapping

input("Press enter to close the window..")
browser.close()