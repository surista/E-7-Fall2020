# reversalShortList.py 
#
# Look for reversals in a file of words
# Usage:
#      % python reversals.py words.txt
#
# Jeff Parker, July, 2018
#
# This version profiles the work

from typing import List
import sys
import cProfile


# Takes a list and returns a list of lower case words
# Given  lst = ['art', 'Rat', 'Radar', 'scam', 'tar', 'vista']
# returns ['rat', 'radar']
#
def find_reversals(words: List[str]) -> List[str]:
    "Look for reversals in a list"

    # Initialize results
    results = []

    # Pop from list and look for reversals
    while len(words) > 0:
        word = words.pop(0)
        rev = word[::-1]
        if (word < rev) and (rev in words) and (word not in results):
            results.append(word)

    # Return with results
    return results


def read_file(filename: str) -> List[str]:
    "Read words from a text file and populate a List"   
    res = []

    try:
        with open(filename, 'r') as words:
            for word in words:
                res.append(word.lower().strip())

        return res

    except FileNotFoundError:
        print(f"Could not find file {filename}")
    except:
        print(f"Could not open file {filename}")

    return []


if (len(sys.argv) != 2):
    print("Usage: python reversals <filename>")
else:

    lst  = read_file(sys.argv[1])
    cProfile.run('revs = find_reversals(lst)')

    print(len(revs))

    for word in revs:
        print(word, word[::-1])
