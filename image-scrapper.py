import urllib3
from bs4 import BeautifulSoup
import requests
import re
import os
import random

episode = str(random.randint(1,2703))

if not os.path.isdir(f"./Existential Comics/{episode}"):
    os.makedirs(f"./Existential Comics/{episode}")

url = 'https://www.existentialcomics.com/comic' + episode
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
img_tags = soup.find_all('img', {'class' : 'comicImg'})
img_urls = [img['src'] for img in img_tags]

for img in img_urls:
    filename = f"./Existential Comics/{episode}" + img.split("/")[-1]
    with open(filename, "wb") as f:
        if 'http' not in img:
            img = '{}{}'.format(url, img)
        response = requests.get(img)
        f.write(response.content)
