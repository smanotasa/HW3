#%%
#!pip3 install -r requirements.txt
from selenium.webdriver.common.keys import Keys
# auxiliary functions modified by Luis.
import scrape_functions as kzd
import sys
import calendar
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
import re
from selenium.webdriver.support.ui import Select
import random
import time
from selenium import webdriver
import os
import numpy as np
import importlib
importlib.reload(sys.modules['scrape_functions'])
from datetime import date
# %% Starting code


geko_path = '/Users/luisquinonespr/code/text_mining/pset3/HW3/geckodriver'


profile, browser, download_path = kzd.start_up()
# Clicking on the different buttoms to input things:
time.sleep(3)


# Click on  place

#%%
place = input('Where do you want to go?')
search1 = browser.find_element('xpath','//input[@placeholder="¿Where do you want to go?"]')
search1.send_keys(place)
#%%
#__bui-c969239-1
# Clik on dates:

kzd.check_and_click(
    browser, '//button[@class="d47738b911 e246f833f7 fe211c0731"]', type='xpath')

#%%
time.sleep(3)
dates=browser.find_elements('xpath',
    '//table[@class="aadb8ed6d3"]/tbody/tr/td/span')

# for el in dates:
#     print(el.get_attribute("data-date"))
#%%
# dates = browser.find_elements('xpath',
#     '//div[@class="bui-calendar__wrapper"]//table[@class="bui-calendar__dates"]//tbody//td[@class!="bui-calendar__date--empty"]')

from_day = input('Day from which you want to look for (In january)')
if int(from_day)< date.today().day:
    print('Wrong from_day')

to_day = input('Day until which you want to look for (In january)')


for date1 in dates:
    if date1.get_attribute("data-date") == f"2023-01-{from_day}":
        # date1.click() this is the old webdriver version
        browser.execute_script("arguments[0].click();", date1)
    if date1.get_attribute("data-date") == f"2023-01-{to_day}":
        # date1.click()
        browser.execute_script("arguments[0].click();", date1)
        break


#%% Click to search:

kzd.check_and_click(
    browser, 'button.d4b6b7a9e7', type='css')
time.sleep(2)
# kzd.check_and_click(browser, 'div._fe1927d9e:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1) > div:nth-child(1)', type='css')


hotels = browser.find_elements('xpath','//div[@class="fcab3ed991 a23c043802"]')
ratings = browser.find_elements('xpath','//div[@class="b5cd09854e d10a6220b4"]')

ratings_list=[]
for i in ratings:
    #print(i.get_attribute('data-testid'))
    print(i.text)
    ratings_list.append(i.text)
hotels_list=[]
for i in hotels:
    #print(i.get_attribute('data-testid'))
    print(i.text)
    hotels_list.append(i.text)

#%% LOOPING OVER WEBPAGES:

"""
This function is to obtain total number of pages.
To loop, just insert the full code on a big loop and use the pages output.


ADDITION: You can also add random waiting times to avoid getting banned from webpages.
"""

time.sleep(2)


def get_number_pages(browser):
    '''
    Get the number of pages.
    '''
    a = browser.find_elements('xpath',
        '//button[text() and @class="fc63351294 f9c5690c58"]')
    total_pages = int(a[-1].text)
    return(total_pages)


pages = get_number_pages(browser)
#From here it is very easy to program a loop that waits and keeps appending results

#
#
#
