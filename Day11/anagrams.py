#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

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

