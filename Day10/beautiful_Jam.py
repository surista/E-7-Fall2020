#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
SpaceJam page
"""

import requests
from bs4 import BeautifulSoup

"prettify print the html of a given url"

url = "https://spacejam.com/"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, 'html.parser')
pretty_soup = soup.prettify()

links = soup.find_all("a")


# image_url = []
# for link in links:
#     alt = link.find('img', alt = True)
#     if alt:
#         if link.find('img')['alt'] == "":
#             print(link)
#         else:
#             image_url.append(link.find('img')['alt'])

# print("\nNumber of links with an an img and alt attribute:", len(image_url))

image_url = {}
for link in links:
    alt = link.find('img', alt = True)
    if alt:
        if link.find('img')['alt'] == "":
            print(link)
        else:
            image_url[link.find('img')['alt']] = link['href']

print(image_url)