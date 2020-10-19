# search.py
#
# Jeff Parker June 2017
#
# Illustrates the use of a function defined in another file`

import utils

def find_all_all_vowels(filename):
    f = open(filename)
    result = []

    for word in f:
        word = word.strip()
        if utils.all_vowels(word):
            result.append(word)

    return result

if __name__ == "__main__":
    lst = find_all_all_vowels('words.txt')
    for word in lst:
        print(word)

