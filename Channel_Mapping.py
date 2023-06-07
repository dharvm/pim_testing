import time
import random
from login import pim_login

def channel_mapping(browser):
    pim_login(browser)
    browser.find_element("xpath",'//span[contains(text(),"Channel")]').click()
    time.sleep(2)
    browser.find_element("xpath",'//a[text()="Mapping"]').click()
    time.sleep(5)

    browser.find_element("xpath",'//span[text()="Map"]').click()
    time.sleep(5)

    # For Select Channel..
    channels = browser.find_elements("xpath",'//select[@id="channel"]//option')
    channels_option_values = [option.get_attribute("value") for option in channels]
    print(channels_option_values,len(channels_option_values))

    ch = browser.find_element("xpath",f'//select[@id="channel"]//option[@value="{channels_option_values[random.randrange(0,len(channels_option_values))]}"]')
    ch.click()
    channel_selected = ch.get_attribute("value")
    print("Selected value is :",channel_selected)
    time.sleep(5)

    # For Your Category..
    select_L1 = browser.find_elements("xpath",'//select[@id="level1"]//option[@value!=""]')
    select_L1_options = [option.get_attribute("value") for option in select_L1]
    print(select_L1_options,len(select_L1_options))

    browser.find_element("xpath",f'//select[@id="level1"]//option[@value="{select_L1_options[random.randrange(1,len(select_L1_options))]}"]').click()
    time.sleep(2)

    for i in range(1,9):
        print("LEVEL ->",i)
        
        
        try:
            level_element = browser.find_element("xpath",f'//select[@id="level{i}"]//option')
            try:
                print(level_element)    
                select_level = browser.find_elements("xpath",f'//select[@id="level{i}"]//option[@value!=""]')
                select_Level_options = [option.get_attribute("value") for option in select_level]
                print(f"level{i} option - >",select_Level_options,len(select_Level_options))
                print(select_Level_options[random.randrange(0,len(select_Level_options))])
                browser.find_element("xpath",f'//select[@id="level{i}"]//option[@value="{select_Level_options[random.randrange(0,len(select_Level_options))]}"]').click()
                time.sleep(2)
                print("2nd Try getting error in Your Category")
            except:
                break
        
        except:
            break
            
        
    # For Core Category..
    if channel_selected == "amazon":
        select_core_L1 = browser.find_elements("xpath",'//select[@id="corelevel1"]//option[@value!=""]')
        select_core_L1_options = [option.get_attribute("value") for option in select_core_L1]
        print(select_core_L1_options,len(select_core_L1_options))

        browser.find_element("xpath",f'//select[@id="corelevel1"]//option[@value="{select_core_L1_options[random.randrange(1,len(select_core_L1_options))]}"]').click()
        time.sleep(2)

        for i in range(1,9):
            print(f"CORE LEVEL {channel_selected} ->",i)
            
            try:
                level_element = browser.find_element("xpath", f'//select[@id="corelevel{i}"]//option')
                try:
                    print(level_element)    
                    select_level = browser.find_elements("xpath",f'//select[@id="corelevel{i}"]//option[@value!=""]')
                    select_Level_options = [option.get_attribute("value") for option in select_level]
                    print(f"corelevel{i} option - >",select_Level_options,len(select_Level_options))
                    print(select_Level_options[random.randrange(0,len(select_Level_options))])
                    browser.find_element("xpath",f'//select[@id="corelevel{i}"]//option[@value="{select_Level_options[random.randrange(0,len(select_Level_options))]}"]').click()
                    time.sleep(2)
                except:
                    print("2nd Try getting error in Core Category Amazon")
                    pass
            
            except:
                break
    elif channel_selected == "magento":
        select_core_L1 = browser.find_elements("xpath",'//select[@id="magentoLevel1"]//option[@value!=""]')
        select_core_L1_options = [option.get_attribute("value") for option in select_core_L1]
        print(select_core_L1_options,len(select_core_L1_options))

        browser.find_element("xpath",f'//select[@id="magentoLevel1"]//option[@value="{select_core_L1_options[random.randrange(1,len(select_core_L1_options))]}"]').click()
        time.sleep(2)

        for i in range(1,9):
            print(f"CORE LEVEL of {channel_selected}->",i)
            
            try:
                level_element = browser.find_element("xpath", f'//select[@id="magentoLevel{i}"]//option')
                try:
                    print(level_element)    
                    select_level = browser.find_elements("xpath",f'//select[@id="magentoLevel{i}"]//option[@value!=""]')
                    select_Level_options = [option.get_attribute("value") for option in select_level]
                    print(f"magentoLevel{i} option - >",select_Level_options,len(select_Level_options))
                    print(select_Level_options[random.randrange(0,len(select_Level_options))])
                    browser.find_element("xpath",f'//select[@id="magentoLevel{i}"]//option[@value="{select_Level_options[random.randrange(0,len(select_Level_options))]}"]').click()
                    time.sleep(2)
                except:
                    print("2nd Try getting error in Core Category in Magento") 
                    pass
            
            except:
                break
    else:
        print(channel_selected,"not valid")
        
    browser.find_element("xpath",'//span[text()="Save"]').click()
    time.sleep(5)
