### Imports
from bs4 import BeautifulSoup

import random as random
import requests
import sys

# Notes: 
# base url: https://transcripts.foreverdreaming.org/viewtopic.php?f=292&t={url substrings}

# season 6 url substrings (must include &sid=f24ccd5eea5bfc2086ee09ad73943b29 after "t={}")
## 18278 - 18289

# season 7 url substrings
## 18290 - 18301

# season 8 url substrings
## 18302 - 18311

# Setting up variables for URL formatting
base_url, start, end, tag = "https://transcripts.foreverdreaming.org/viewtopic.php?f=292&t={}{}", 18278, 18311, "&sid=f24ccd5eea5bfc2086ee09ad73943b29"

# redirecting output to file (so we can have "data points")
orig_stdout = sys.stdout
f = open('transcripts.txt', 'w')
sys.stdout = f

# Collect all those urls
urls_to_scrape = []
for i in range(start, end+1):
    urls_to_scrape.append(base_url.format(i, tag if i <= 18289 else ""))

# just doin a lil scrapin, u kno wut im sayin?
for URL in urls_to_scrape:
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="postbody").find_all("p")

    for element in results:
        print(element.text)

# redirecting output to o.g.
sys.stdout = orig_stdout
f.close()
