#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Use matplotlib to draw a histogram of the word lengths
"""

import matplotlib.pyplot as plt
from collections import Counter

def wordLengths(filepath):
    sol = {}
    try:
        with open(filepath, 'r') as f:
            words_list = [word.strip() for word in f]

    except FileNotFoundError:
        print(f"Houson, we have a problem, could not find file {filepath}")

    # create dictionary for counting
    for word in words_list:
        if len(word) not in sol:
            sol[len(word)] = 1
        else:
            sol[len(word)] += 1

    return sorted(sol.items())

def plot_histogram(filepath):
    "create a histogram of wordLengths"
    x,y = zip(*wordLengths(filepath))
    plt.bar(x,y,color='g')
    plt.show()

filepath = 'words.txt'
print(wordLengths(filepath))
plot_histogram(filepath)

