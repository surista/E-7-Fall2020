#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Use matplotlib to draw a histogram of the word lengths
"""

import matplotlib.pyplot as plt


def wordLengths(filepath):
    sol = {}
    try:
        with open(filepath, 'r') as f:
            raw_list = [word.strip() for word in f]

    except FileNotFoundError:
        return f"Houson, we have a problem, could not find file {filepath}"

    # create dictionary for counting
    for word in raw_list:
        if len(word) not in sol:
            sol[len(word)] = 1
        else:
            sol[len(word)] += 1
    # return sorted list of tuples
    return sorted([(x, y) for x, y in sol.items()])

def plot_histogram(filepath):
    "create a histogram of wordLengths"
    x,y = zip(*wordLengths(filepath))
    plt.bar(x,y,color='b')
    plt.show()

filepath = 'words.txt'
plot_histogram(filepath)

