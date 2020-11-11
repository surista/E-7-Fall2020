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

        bank = {}

        for word in words_list:
            reversed_word = (''.join(sorted(word)))
            try:
                lst = bank[reversed_word]
                lst.append(word)

            except KeyError:
                bank[reversed_word] = [word]



    except FileNotFoundError:
        print(f"Houson, we have a problem, could not find file {filepath}")

    sol = []
    for x in bank:
        word = bank[x]
        if len(x) > 1:
            sol.append((len(word), word))

    x = sorted(sol,key=lambda x:(-x[0]))
    return x[0:10]


filename = "words.txt"
print(find_anagrams(filename))

