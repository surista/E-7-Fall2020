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

links = soup.find_all("a")

print(links)
# all_links = [(link['href'], link.string) for link in soup.find_all("a")]
# print(all_links, len(all_links))

# all_links = [(link, link.string) for link in soup.find_all("a")]
# print(all_links, len(all_links))
#
# for link i all_links:
#     if
#
#
# all_links = [link for link in soup.find_all("a")]
# print(len(all_links))
# for item in all_links:
#     print(item)
