# save_url.py
# S. Urista / 4 Oct 2020
# Usage:
# python save_url.py <website> <textfile>

import urllib.request
import sys


def fetch_contents(website, filename):
    "Saves the contents of a webpage to a file"
    try:
        res = []

        with urllib.request.urlopen(website) as f:
            text = f.read().decode('utf-8')

        # Break the page into lines
        text = text.split('\n')
        for line in text:
            res.append(line)

        # print contents to file
        with open(filename, 'w') as f:
            for line in text:
                print(line, file=f)

        return res

    except urllib.error.URLError as e:
        print(e.reason)
        return []

