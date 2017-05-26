# load dependencies
from __future__ import division
import requests
import sys
import os
from bs4 import BeautifulSoup
import re

'https://www.youtube.com/api/timedtext?&v={video_id}&lang={language_code}'

link = 'https://www.youtube.com/watch?v=BPMUz1l8rpA'

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

main_url = 'https://www.youtube.com/api/timedtext?&v=BPMUz1l8rpA&lang=en'

req = requests.get(main_url)
soup = BeautifulSoup(req.content, 'html5lib')
text_tags = soup.find_all('text')

for i in text_tags:
    text_tag_content = list_to_string(i.contents)
    text_tag_t_start = list_to_string(i['start'])
    text_tag_t_dur = list_to_string(i['dur'])
    print('CONTENT:' + text_tag_content)
    print('START:' + text_tag_t_start)
    print('DURATION:' + text_tag_t_dur)
