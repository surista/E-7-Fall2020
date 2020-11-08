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


image_url = {}
for link in links:
    alt = link.find('img', alt = True)
    if alt:
        if link.find('img')['alt'] == "":
            print(link)
        else:
            if link['href'].startswith('https'):
                image_url[link.find('img')['alt']] = link['href']
            else:
                image_url[link.find('img')['alt']] = "https://spacejam.com/"+link['href']
print("\nNumber of links with an an img and alt attribute:", len(image_url))

print(image_url['Jam Central'])


def test_image_url():
    assert (image_url['Jam Central'] == 'https://spacejam.com/cmp/jamcentral/jamcentralframes.html')
    assert (image_url['Junior Jam'] == 'https://spacejam.com/cmp/junior/juniorframes.html')
    assert (image_url['Warner Studio Store'] == 'https://www.wbshop.com/')
    assert (image_url['Behind the Jam'] == 'https://spacejam.com/cmp/behind/behindframes.html')

    print("Success!")


test_image_url()