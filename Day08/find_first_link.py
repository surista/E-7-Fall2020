#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
takes a URL and finds the first link on the page
"""

import urllib.request


# Note that the python.org link may differ depending on browser of choice.

import urllib.request

def find_first_link(url):
    """Returns the first URL and link txt on page"""

    # read in url text
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')

    # set up tags for searching, find first link anchor.

    href_tag = '<a'
    first_href = text.find(href_tag)
    end_href = text.find('>', first_href + 1)

    link_end = text.find('</a')
    link_start = text.rfind(">", 1,link_end)

    # generate string segments
    first_url = text[first_href + 3:end_href]  # +3 offsets <a
    first_text = text[link_start+1:link_end].strip()

    return (first_url, first_text)

for url in ['http://www.python.org/', 'https://www.extension.harvard.edu', 'http://en.wikipedia.org/wiki/Python']:
    print(f"{url}\n\t{find_first_link(url)}")

print('Done')