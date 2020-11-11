#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
find anagrams in list of words
"""

from typing import List
from collections import OrderedDict

def find_anagrams(path: str) -> List:
    """
    "Find the largest set of anagrams, return as sorted list"
    """
    try:
        with open(path, 'r') as f:
            words_list = [word.strip() for word in f]

        reversed_word = [(''.join(sorted(word))) for word in words_list]


    except FileNotFoundError:
        print(f"Houson, we have a problem, could not find file {filepath}")

    print(reversed_word[0:10])
    print(words_list[0:10])

    sol = {}
    for x in words_list:
        if x not in sol:
            sol[x] = 1
        else:
            sol[x] += 1

    rev = [(x, y) for y, x in sol.items()]

    return None

filename = "words.txt"
print(find_anagrams(filename))

