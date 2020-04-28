# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:51:07 2020

@author: samson
"""

from selenium import webdriver
from threading import Thread
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time, os 

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:/Users/samson/AppData/Local/Google/Chrome/User Data")


driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)
driver.get("https://web.whatsapp.com/")#Add the webhost name
wait = WebDriverWait(driver, 3000)
try:
    
    name = str(input('enter your friend name'))
          
    arg= '//*[contains(@title,"{}")]'.format(name)


    user = driver.find_element_by_xpath(arg)
    user.click()
    if name:
        

        msg = str(input('enter your message'))
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

        for i in range(1):
                msg_box.send_keys(msg)
                button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
                button.click()
except Exception as e:
    print(e)
  

    return None


