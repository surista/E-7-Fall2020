#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

import urllib.request
import string
import re

def find_links(website):
    "Return a list of the links on this page: Use only urllib and Regular Expressions"
    pass


def find_first_link(url):
    """Returns the first URL and link txt on page"""

    # read in url text
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')

    links = re.findall('<a.*/a>', text)

    return links

website = 'https://www.extension.harvard.edu'
sol = find_first_link(website)

print(len(sol))
for x in sol:
    print(x)