# load dependencies
from __future__ import division
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains


import time
import requests
import sys
import os
import csv
from bs4 import BeautifulSoup
import re
import datetime

def get_youtube_id(link):
    id = re.findall(r'/?v=(.*)', link)
    id_string = list_to_string(id)
    return(id_string)

def get_language_code(link):
    lang_code_output = 'en'
    return(lang_code_output)

def list_to_string(list_input):
    string_output = ''.join(list_input)
    return(string_output)

def create_transcript_url(link):
    video_id = get_youtube_id(link)
    video_language_code = get_language_code(link)
    custom_url = 'https://www.youtube.com/api/timedtext?&v='+video_id+'&lang=' + video_language_code
    return(custom_url)

def write(filename, data):
    filename += ".csv"
    failure_count = 0
    with open(filename, 'w') as csvfile:
        fieldnames = ['content', 'start', 'duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        if len(data) > 0:
            for row in data:
                writer.writerow({'content': row[0], 'start': row[1], 'duration': row[2]})
        else:
            failure_count += 1
    return(failure_count)

# ============================== AUTOMATIC CAPTIONS ========================================================
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/watch?v=wOn8xawC-HQ')

# this seems to work fine
element = driver.find_element_by_xpath("//button[contains(@class, 'yt-uix-button')]")
element.click()

time.sleep(5)

# Here is the problem (selenium.common.exceptions.ElementNotInteractableException)
element = driver.find_element_by_xpath("//button[contains(@class, 'yt-uix-menu-close-on-select')]")
element.click()

# Here we should add another timeout in order to wait for the transcript to show up

# Here we can use the code as below to get the transcript

# Afterwards we could add the retrieval of metadata (view, thumbs up, down etc.)



# ==========================================================================================================

main_url = ['https://www.youtube.com/watch?v=wOn8xawC-HQ']

for url in main_url:
    failure_count = 0
    id = get_youtube_id(url)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html5lib')
    text_tags = soup.find_all('text')
    data = []
    for i in text_tags:
        text_tag_content = list_to_string(i.contents)
        text_tag_t_start = list_to_string(i['start'])
        text_tag_t_dur = list_to_string(i['dur'])
        if text_tag_content != "":
            data.append([text_tag_content, text_tag_t_start, text_tag_t_dur])
    failure_count += write(id, data)
#print("Successful: " + str(len(main_url) - failure_count) + "; Failed: " + str(failure_count))


#################################################
#######NEW FLOW
from __future__ import division
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains

import time
import requests
import sys
import os
import csv
from bs4 import BeautifulSoup
import re
import datetime


#if XML method does not work
#access url
url = 'https://www.youtube.com/watch?v=wOn8xawC-HQ'

phantom_driver = webdriver.PhantomJS(executable_path="./phantomjs-2.1.1-macosx/bin/phantomjs")

phantom_driver.get(url)

print(len(phantom_driver.page_source))

#from SO https://stackoverflow.com/questions/44657787/clicking-on-dynamically-loaded-menu-with-python-phantomjs/44761388#44761388

#click on "more"
phantom_driver.find_element_by_xpath('//*[@id="action-panel-overflow-button"]').click()

print(len(phantom_driver.page_source))

#click on "transcript" in the opened menu
phantom_driver.find_element_by_xpath('//*[@class="yt-ui-menu-item has-icon yt-uix-menu-close-on-select action-panel-trigger action-panel-trigger-transcript"]').click()

print(len(phantom_driver.page_source))


#click on "English (automatic captions)"
#Dynamic id?
phantom_driver.find_element_by_xpath('//*[@id="kbd-nav-179867"]').click()

print(len(phantom_driver.page_source))

#click on the dropdown choice
phantom_driver.find_element_by_xpath('//*[@id="yt-ui-menu-item yt-uix-menu-close-on-select yt-uix-button-menu-item"]').click()

print(len(phantom_driver.page_source))

#get the new DOM
html = phantom_driver.find_element_by_tag_name('html').get_attribute('innerHTML')

print('transcript-scrollbox' in html)

soup = BeautifulSoup(html, "html5lib")

transcript_div = soup.find_all('div', {'id': 'transcript-scrollbox'})

subs_divs = transcript_div.find('div')


#################################################











# print(phantom_driver.page_source)
#
# print("yt-uix-button" in phantom_driver.page_source)
#
# phantom_driver.find_element_by_xpath("//button[contains(@class, 'yt-uix-button')]").click()
phantom_driver.find_element_by_id('action-panel-overflow-button').click()

#? do we need to get the DOM again after the click?

#try to click on dynamic drop down
dyn_drop_down = phantom_driver.find_element_by_id('action-panel-overflow-button').click()
for sub in dyn_drop_down.find_elements_by_id('action-panel-overflow-menu'):
    print(sub)
    # if option.text == 'BMW':
    #     option.click() # select() in earlier versions of webdriver
    #     break


full_class_of_trigger = 'yt-ui-menu-item has-icon yt-uix-menu-close-on-select action-panel-trigger action-panel-trigger-transcript'
print(full_class_of_trigger in phantom_driver.page_source)

phantom_driver.findElement(By.className(full_class_of_trigger));

print(phantom_driver.page_source)

phantom_driver.find_element_by_class_name('action-panel-trigger-transcript').click()


#via JavaScript (example)
#execute_script("$('#calendarbody > div:nth-child(12) > div.col-sm-2.calendar-home-weekly > button').click()")

time.sleep(5)

phantom_driver.find_element_by_xpath("//button[contains(@class, 'yt-uix-button-content')]").click()

time.sleep(5)

print(phantom_driver.page_source)
