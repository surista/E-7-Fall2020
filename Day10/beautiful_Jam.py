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
soup = BeautifulSoup(html_content, 'html.parser')
all_links = [link for link in soup.find_all("a")]
test = []
for item in all_links:
    print(item[0:5])

print(test)