#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
find anagrams in list of words
"""

from typing import List
from collections import defaultdict

def find_anagrams(path: str) -> List:
    """
    "Find the largest set of anagrams, return as sorted list"
    """

    try:
        with open(path, 'r') as f:
            words_list = [word.strip() for word in f]

        # create list of all words sorted alphabetically
        sorted_words = [(''.join(sorted(word))) for word in words_list]

    except FileNotFoundError:
        print(f"Houston, we have a problem, could not find file {path}")

    # pair each word to its sorted self
    pairs = [(sorted_words[x], words_list[x]) for x in range(len(words_list))]

    # defaultdict - sidesteps KeyErrors!
    agrams =defaultdict(list)
    for x, y in pairs:
        agrams[x].append(y)

    #items of length 1 means not an anagram
    sol = []
    for item in agrams:
        if len(agrams[item]) > 1:
            sol.append((len(agrams[item]),agrams[item]))

    return sorted(sol, reverse=True)

filename = "words.txt"
lst = find_anagrams(filename)
for anagram in lst[:5]:
    print(anagram)
