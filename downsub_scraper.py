import urllib.parse
import re, csv
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup as bs, SoupStrainer
import wget, os, sys, httplib2, requests, shutil, time


# Source: https://stackoverflow.com/a/5251383
def slugify(value):
    filename = re.sub(r'[/\\:*?"<>|]', '', value)

    return filename


# Download transcript given a url and a title.
def download_transcript(url, title):
    orig = "http://downsub.com/?url="
    encode = urllib.parse.quote(url, safe='')
    target_url = orig + encode

    http = httplib2.Http()
    status, response = http.request(target_url)

    links = []
    for link in bs(response, parseOnlyThese=SoupStrainer('a')):
        links.append(link)

    target_link = str(links[2])
    start = target_link.find('"')
    end = target_link.rfind('"')

    download_link = ("http://downsub.com" + target_link[(start+2):end]).replace("amp;", "", 1)

    # Solution derived from https://stackoverflow.com/a/34695096
    req = requests.get(download_link, stream=True)

    if req.status_code == 200:
        with open("output_dir/" + slugify(title) + ".txt", 'wb') as f:
            req.raw.decode_content = True
            shutil.copyfileobj(req.raw, f)


# ======================== Main ========================
# Each element is a tuple of (url, title)
# Example
# data = [
#     ["https://www.youtube.com/results?search_query=cat+fail+glass+door", "4"],
#     ["https://www.youtube.com/watch?v=2y7rk7eHHAM", "5"],
#     ["https://www.youtube.com/watch?v=g_PtkN3aYFo", "6"]
# ]

header = False
with open('youtube_data.csv', 'r') as f:
    reader = csv.reader(f)

    for element in reader:
        if header == False:
            header = True
        else:
            try:
                download_transcript(element[0], element[1])
            except:
                print("Video " + element[1] + " not supported.")
