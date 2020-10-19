#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
takes a URL and finds the first link on the page
"""

import urllib.request
import sys


def find_url(website):
    """Returns the first URL and link txt on page"""

    # read in url text
    with urllib.request.urlopen(website) as f:
        text = f.read().decode('utf-8')

    # set up tags for searching, find first link anchor.
    # 9 refers to length of the <a href=" tag

    href_tag = '<a href="'
    first_href = text.find(href_tag)
    end_href = text.find('"', first_href + 9)

    link_end = text.find('</a')
    link_start = text.rfind(">", 1,link_end)

    # generate string segments
    first_url = text[first_href + 9:end_href]
    first_text = text[link_start+1:link_end].strip()

    return (first_url, first_text)


url = 'https://www.harvard.edu/'
print(find_url(url))