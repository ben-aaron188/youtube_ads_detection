import urllib.parse
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup as bs, SoupStrainer
import wget, os, sys, httplib2, requests, shutil, time

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

    req = requests.get(download_link, stream=True)
    if req.status_code == 200:
        with open(title + ".txt", 'wb') as f:
            req.raw.decode_content = True
            shutil.copyfileobj(req.raw, f)


# ======================== Main ========================
# Each element is a tuple of (url, title)
# Example
data = [
    ["https://www.youtube.com/results?search_query=cat+fail+glass+door", "1"],
    ["https://www.youtube.com/watch?v=2y7rk7eHHAM", "2"],
    ["https://www.youtube.com/watch?v=g_PtkN3aYFo", "3"]
]

for element in data:
    try:
        download_transcript(element[0], element[1])
    except:
        print("Video " + element[1] + " not supported.")
