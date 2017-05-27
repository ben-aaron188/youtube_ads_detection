# load dependencies
from __future__ import division
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

    with open(filename, 'w') as csvfile:
        fieldnames = ['content', 'start', 'duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        if len(data) > 0:
            for row in data:
                writer.writerow({'content': row[0], 'start': row[1], 'duration': row[2]})

# ================================================================================================

main_url = ['https://www.youtube.com/api/timedtext?&v=BPMUz1l8rpA&lang=en',
            'https://www.youtube.com/watch?v=9_VKSDTdHOg'
]

for url in main_url:
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

    write(id, data)
