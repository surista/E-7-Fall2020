#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
SpaceJam page
"""

import requests
from bs4 import BeautifulSoup

url = "https://spacejam.com/"
html_content = requests.get(url).text

webpage = requests.get("https://spacejam.com")
soup = BeautifulSoup(html_content, 'html.parser')
pretty_soup = soup.prettify()
print(pretty_soup)
all_links = [link for link in soup.find_all("a")]
test = []
# for item in range(6):
#     print(all_links[item])

# print(test)

