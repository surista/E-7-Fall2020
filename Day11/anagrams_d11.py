#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
find anagrams in list of words
"""

from typing import List

def find_anagrams(path: str) -> List:
    """
    "Find the largest set of anagrams, return as sorted list"
    """
    try:
        with open(path, 'r') as f:
            words_list = [word.strip() for word in f]

    except FileNotFoundError:
        print(f"Houson, we have a problem, could not find file {filepath}")

    sol = {}
    count = 0
    for wrd in range(len(words_list)-2):
        are_anagrams(words_list[count], words_list[count+1])

    # must be same length
    if len(word1) != len(word2):
        return False

    # can't be the same word
    if word1 == word2:
        return False

    # sort each string alphabetically and compare
    return sorted(word1.lower()) == sorted(word2.lower())

def are_anagrams(word1, word2):
    # Are the two words anagrams?

    # must be same length
    if len(word1) != len(word2):
        return False

    # can't be the same word
    if word1 == word2:
        return False

    # sort each string alphabetically and compare
    return sorted(word1.lower()) == sorted(word2.lower())


filename = "shorter.txt"
print(find_anagrams(filename))