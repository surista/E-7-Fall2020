# DoublesPick.pyG
#
# Which pairs of words are separated by a double letter?
#
# Usage:
#       % python doublesPick.py
#
# Jeff Parker
#
# Oct 2017

import sys

from tkinter import Tk
from tkinter.filedialog import askopenfilename


# Build a Dictionary of all words
# Takes a file, and returns a dictionary
#
def build_dict(fin):
    words = {}

    # Take each line, strip \n, add to dictionary
    for word in fin:
        word = word.strip()

        # Dictionary as a Set idiom
        # Add to our set of words
        words[word] = None

    return words


# Takes a string, and finds all pairs of double letters
# Returns a list of positions: 
# find_doubles('mississippi') returns  [2, 5, 8]
# 
def find_doubles(word):
    doubles = []
    for pos in range(len(word) - 1):
        if word[pos] == word[pos+1]:
            doubles.append(pos)

    return doubles


# Create a list of all pairs: words of the form 
# ['accretes', 'aretes']
#
def build_list(d):
    res = []

    # Take each word in the dictionary, and see if we can find a pair
    for word in d:
        positions = find_doubles(word)
        for pos in positions:
            cand = word[:pos] + word[pos+2:]
            if (cand in d):
                res.append([word, cand])

    return res


# Main routine to do the work
# Takes a file, and returns a list of pairs
#
def find_pairs(fileName):
    # Build a dictionary of all words
    try:
        with open(fileName) as fin:
            d = build_dict(fin)
    except FileNotFoundError:
        print("File", fileName, "was not found")
        return []
    except: 
        print("Error processing file")
        return []

    # Filter for words that appear again when we strip a pair of double letters
    # This list will be unsorted, as we were traversing dictionary
    lst = build_list(d)

    # Sort the list
    lst.sort()

    return lst

Tk().withdraw() # Don't need a full GUI
filename = askopenfilename() # show an "Open" dialog box 

lst = find_pairs(filename)

print(len(lst))

# Print the first 10 in the list
for word in lst[:10]:
    print(word) 
