#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
find anagrams in list of words
"""


def are_anagrams(word1, word2):
    # Are the two words anagrams?

    if len(word1) != len(word2):
        return False

    if word1 == word2:
        return False

    word1, word2 = sorted(word1.lower()), sorted(word2.lower())

    return word1 == word2