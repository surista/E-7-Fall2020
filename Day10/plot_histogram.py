#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Use matplotlib to draw a histogram of the word lengths
"""

filepath="words.txt"
import matplotlib.pyplot as plt
import numpy as np

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


import matplotlib.pyplot as plt


# bar chart showing frequency per word length

def plot_histogram(filepath):
    "create a bar chart - not histogram - of wordLengths"
    x, y = zip(*wordLengths(filepath))
    plt.bar(x, y)
    plt.show()


def plot_histogram_new(filepath):
    "create a bar chart that looks like a histogram"
    x, y = zip(*wordLengths(filepath))
    plt.bar(x, y, width=1, edgecolor='black')
    plt.show()