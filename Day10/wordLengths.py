#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Creates a list with tuples holding the number of words of each word length
"""
import cProfile
def wordLengths(filepath):
    sol = {}
    try:
        with open(filepath, 'r') as f:
            words_list = [word.strip() for word in f]

    except FileNotFoundError:
        return f"Houson, we have a problem, could not find file {filepath}"

    # create dictionary for counting
    for word in words_list:
        if len(word) not in sol:
            sol[len(word)] = 1
        else:
            sol[len(word)] += 1

   # return sorted list of tuples
    return sorted([(x, y) for x, y in sol.items()])

filepath = 'words.txt'
cProfile.run('test = wordLengths(filepath)')
